import requests
from bs4 import BeautifulSoup
from saver import Saver

class Scrapper:
    def __init__(self, start_url, savefile):
        self.parser = Parser()
        self.start_url = start_url
        self.saver = Saver(savefile)

    def start_scrapping(self, url=None):
        if url == None:
            url = self.start_url
        nested_urls = self.step_down(url)
        if not url == self.start_url:
            return
        elif nested_urls == None:
            return
        else:
            for url in nested_urls:
                self.step_down(url)

    def step_down(self, root_url):
        try:
            response = requests.get(root_url)
            web_page = response.content
            urls = self.parser.get_links(web_page)
            self.saver.save(root_url, urls)
        except Exception:
            return None
        return urls

class Parser:
    def get_links(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]


