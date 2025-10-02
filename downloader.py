import re, requests, bs4, os


class Downloader:
    list = None
    cache_folder = "cache"

    ficton_id = None

    def __init__(self, url):
        #Example
        #https://www.royalroad.com/fiction/48893/the-dungeon-without-a-system

        #Extractin' fiction ID
        #Check if valid URL
        if re.match(r"^(https://)?(www\.)?royalroad\.com/fiction/\d+/\w+", url):
            self.ficton_id = re.search(r'\d+', url)[0]
        else:
            raise Exception
        
        #Full Url
        self.url = "https://www.royalroad.com/fiction/" + self.ficton_id

        #Creatin' folders
        if not os.path.exists(self.cache_folder):
            os.mkdir(self.cache_folder)

        self.folder_path = self.cache_folder + "/" + self.ficton_id
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        os.chdir(self.folder_path)

    def get_url_list(self):
        soup = bs4.BeautifulSoup(requests.get(url=self.url).content, features="html.parser")

        list = []

        for row in soup.find_all(class_ = "chapter-row"):
            chapter = {}

            table_chap = row.find_all("a")
            chapter["name"] = table_chap[0].contents[0].strip()
            chapter["date"] = table_chap[1].find("time")["datetime"].split("T")[0]
            chapter["url"] = "https://www.royalroad.com" + table_chap[1]["href"]

            list.append(chapter)

        self.list = list
        return list
    
    def download(self):
        if not self.list:
            self.get_url_list()
        
        for chapter in self.list:
            chapter_id = chapter["url"].split("/")[7]

            if not os.path.exists(chapter_id):
                os.mkdir(chapter_id)
                soup = bs4.BeautifulSoup(requests.get(self.url + "/" + chapter_id))

if __name__ == "__main__":
    g = Downloader("https://www.royalroad.com/fiction/33844/the-runesmith")
    g.download()