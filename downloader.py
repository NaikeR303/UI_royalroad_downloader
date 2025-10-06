import re, requests, bs4, time, os, shutil, weasyprint


class Downloader:
    fic_cover = {}
    list = []
    list_d = []

    redownload = False

    cache_folder = "cache"
    fic_folder = None

    ficton_id = None

    def __init__(self, url):
        #Example
        #https://www.royalroad.com/fiction/134167/sector-bomb

        #Extractin' fiction ID
        #Check if valid URL
        if re.match(r"^(https://)?(www\.)?royalroad\.com/fiction/\d+/\w+", url):
            self.ficton_id = re.search(r'\d+', url)[0]
        else:
            raise Exception
        
        #Full Url
        self.url = "https://www.royalroad.com/fiction/" + self.ficton_id

        #Cache
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)

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

            self.list.append(chapter)

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

        return self.list
    
    def download(self, output = True):
        if not self.list:
            self.get_url_list()

        #Checking cache
        self.list_d = os.listdir(self.fic_folder)
        
        for i in range(len(self.list)):
            chap_id = re.findall(r'\d+', self.list[i]["url"])[1]
            chap_folder = self.fic_folder + "/" + chap_id

            #Reading cache or downloading
            if chap_id in self.list_d:
                with open(chap_folder + "/" + "cache.txt", "r") as file:
                    self.list[i]["content"] = file.read()
            else:
                soup = bs4.BeautifulSoup(requests.get(url=self.list[i]["url"]).content, features="html.parser")
                text = soup.find("div", class_="chapter-inner chapter-content").contents
                self.list[i]["content"] = "".join(str(item) for item in text).strip()

            #Creating cache
            if not os.path.exists(chap_folder):     
                os.mkdir(chap_folder)

                with open(chap_folder + "/cache.txt", "w") as file:
                    file.write(self.list[i]["content"])
            

            if chap_id in self.list_d:
                if output:
                    print(f"{self.list[i]["name"]} is already downloaded! ({i+1}/{len(self.list)})")
            else:
                if output:
                    print(f"Downloaded {self.list[i]["name"]} ({i+1}/{len(self.list)})")

                #A bit of wait to not get banned
                time.sleep(0.5)
            
        return self.list
    
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

        for i in range(len(self.list)):
            file.write(f"\n\n{self.list[i]["name"]}\nDate: {self.list[i]["date"]}\n\n")

            content = self._get_text(self.list[i]["content"])

            for c in content:
                file.write(c + "\n")

    def _create_html(self, template = "html_template_1.html"):
        body = f'<h1><a href="{self.url}">{self.fic_cover['name']}</a></h1>\n<h2>by {self.fic_cover["author"]}</h2>\n<br>\n<br>\n'

        for i in range(len(self.list)):
            body += f"<h2>{self.list[i]["name"]}</h2>\n"
            body += f"<h3>{self.list[i]["date"]}</h3>\n"
            body += f"<div>{self.list[i]["content"]}</div>\n<br>\n<br>\n<br>\n"

        with open(template, "r") as template:
            html = template.read()
            html = html.replace("$$$NAME$$$", self.fic_cover["name"]).replace("$$$BODY$$$", body)

        return html
            
    def to_html(self):
        with open(self._get_filename(self.fic_cover["name"]) + ".html", "w") as file:
            file.write(self._create_html(template="html_template_1.html"))

    def to_pdf(self, output = True): #TODO: Split into files by 100 chapters
        if output:
            print("Creating PDF file, it'll take some time. Please wait...")
        html = weasyprint.HTML(string=self._create_html(template="html_template_2.html"))
        html.write_pdf(self._get_filename(self.fic_cover["name"]) + ".pdf")


if __name__ == "__main__":
    # if os.path.exists("cache"):
    #     shutil.rmtree("cache")


    g = Downloader("https://www.royalroad.com/fiction/98242/magical-engineering-progression-fantasy-litrpg")
    g.download()
    # g.to_txt()
    g.to_html()
    # g.to_pdf()