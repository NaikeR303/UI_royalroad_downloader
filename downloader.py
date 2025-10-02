import re, requests, bs4, os


class Downloader:
    list = None

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

    def get_url_list(self):
        soup = bs4.BeautifulSoup(requests.get(url=self.url).content, features="html.parser")

        list = []

        for row in soup.find_all(class_ = "chapter-row"):
            chapter = {}

            table_chap = row.find_all("a")
            chapter["name"] = table_chap[0].contents[0].strip()
            chapter["date"] = table_chap[1].find("time")["datetime"].split("T")[0]
            chapter["url"] = "https://www.royalroad.com" + table_chap[1]["href"]

            chapter["content"] = None

            list.append(chapter)

        self.list = list
        return list
    
    def download(self):
        if not self.list:
            self.get_url_list()
        
        for chapter in self.list:
            soup = bs4.BeautifulSoup(requests.get(chapter["url"]))

if __name__ == "__main__":
    g = Downloader("https://www.royalroad.com/fiction/33844/the-runesmith")
    print(g.get_url_list())