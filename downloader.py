import re, requests, bs4, time, os, shutil, weasyprint


class Downloader:
    def __init__(self):
        #Example
        #https://www.royalroad.com/fiction/134167/sector-bomb

        self.debug = False

        #Variables
        self.fic_cover = {}
        self.list_chap = []
        self.list_d = []

        self.redownload = False

        self.chap_num = 0
        self.chap_downloaded = 0

        self.cache_folder = "cache"
        self.fic_folder = None

        self.ficton_id = None

        #Cache
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)

    def set_url(self, url):
        #Extractin' fiction ID
        #Check if valid URL
        if re.match(r"^(https://)?(www\.)?royalroad\.com/fiction/\d+/\w+", url):
            self.ficton_id = re.search(r'\d+', url)[0]
        else:
            raise Exception
        
        #Full Url
        self.url = "https://www.royalroad.com/fiction/" + self.ficton_id

    def get_url_list(self):
        soup = bs4.BeautifulSoup(requests.get(url=self.url).content, features="html.parser")

        #URL list
        for row in soup.find_all(class_ = "chapter-row"):
            chapter = {}

            table_chap = row.find_all("a")
            chapter["name"] = table_chap[0].contents[0].strip()
            chapter["date"] = table_chap[1].find("time")["datetime"].split("T")[0]
            chapter["url"] = "https://www.royalroad.com" + table_chap[1]["href"]

            chapter["content"] = None

            self.list_chap.append(chapter)

        #Name, author
        #TODO: Image 
        self.fic_cover["name"] = soup.find(class_ = "fic-title").find("h1").text
        self.fic_cover["author"] = soup.find(class_ = "mt-card-content").find("h3").text.strip()

        #Cache
        self.fic_folder = self.cache_folder + "/" + self.ficton_id
        if not os.path.exists(self.fic_folder):
            os.mkdir(self.fic_folder)
        #Deleting if redownload
        elif self.redownload:
            shutil.rmtree(self.fic_folder)
            os.mkdir(self.fic_folder)

        self.chap_num = len(self.list_chap)

        return self.list_chap
    
    def download(self):
        if not self.list_chap:
            self.get_url_list()

        #Checking cache
        self.list_d = os.listdir(self.fic_folder)
        
        for i in range(self.chap_num):
            chap_id = re.findall(r'\d+', self.list_chap[i]["url"])[1]
            chap_file = self.fic_folder + "/" + chap_id

            #Reading cache or downloading
            if chap_id in self.list_d:
                with open(chap_file, "r") as file:
                    self.list_chap[i]["content"] = file.read()
            else:
                soup = bs4.BeautifulSoup(requests.get(url=self.list_chap[i]["url"]).content, features="html.parser")
                text = soup.find("div", class_="chapter-inner chapter-content").contents
                self.list_chap[i]["content"] = "".join(str(item) for item in text).strip()

            #Creating cache
            if not os.path.exists(chap_file):     
                with open(chap_file, "w") as file:
                    file.write(self.list_chap[i]["content"])
            

            if chap_id in self.list_d:
                if self.debug:
                    print(f"{self.list_chap[i]["name"]} is already downloaded! ({i+1}/{self.chap_num})")
            else:
                if self.debug:
                    print(f"Downloaded {self.list_chap[i]["name"]} ({i+1}/{self.chap_num})")

                #A bit of wait to not get banned
                time.sleep(0.5)

            #Number downloaded
            self.chap_downloaded = i+1
    
    def _get_text(self, content):
        #Get text from chapter in array
        soup = bs4.BeautifulSoup(str(content), features="html.parser")

        text = []

        for div in soup.find_all("p"):
            text.append(div.text)

        return text
    
    def _get_filename(self, name):
        name = str(name).lower()
        name = re.sub(r'[^a-z0-9]+', '_', name)
        name = name.strip("_")

        return(name)
    
    def to_txt(self):
        # if not self.list:
        #     self.download()

        file = open(self._get_filename(self.fic_cover["name"]) + ".txt", "w")

        #Title
        file.write(f"{self.fic_cover["name"]}\nBy {self.fic_cover["author"]}\n")

        for i in range(len(self.list_chap)):
            file.write(f"\n\n{self.list_chap[i]["name"]}\nDate: {self.list_chap[i]["date"]}\n\n")

            content = self._get_text(self.list_chap[i]["content"])

            for c in content:
                file.write(c + "\n")

    def _create_html(self, template):
        body = f'<h1><a href="{self.url}">{self.fic_cover['name']}</a></h1>\n<h2>by {self.fic_cover["author"]}</h2>\n<br>\n<br>\n'

        for i in range(len(self.list_chap)):
            body += f"<h2>{self.list_chap[i]["name"]}</h2>\n"
            body += f"<h3>{self.list_chap[i]["date"]}</h3>\n"
            body += f"<div>{self.list_chap[i]["content"]}</div>\n<br>\n<br>\n<br>\n"

        with open(template, "r") as template:
            html = template.read()
            html = html.replace("$$$NAME$$$", self.fic_cover["name"]).replace("$$$BODY$$$", body)

        return html
            
    def to_html(self, template):
        with open(self._get_filename(self.fic_cover["name"]) + ".html", "w") as file:
            file.write(self._create_html(template=template))

    def to_pdf(self, template): #TODO: Split into files by 100 chapters
        if self.debug:
            print("Creating PDF file, it'll take some time. Please wait...")

        html = weasyprint.HTML(string=self._create_html(template=template))
        html.write_pdf(self._get_filename(self.fic_cover["name"]) + ".pdf")


if __name__ == "__main__":
    # if os.path.exists("cache"):
    #     shutil.rmtree("cache")


    g = Downloader()
    g.set_url("https://www.royalroad.com/fiction/134167/sector-bomb")
    g.get_url_list()
    g.download()
    # g.to_txt()
    g.to_html("templates/html/antique.html")
    # g.to_pdf()