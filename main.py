import requests
from bs4 import BeautifulSoup
from saver import Saver

class Scrapper:
    def __init__(self, start_url, savefile, max_depth=10, max_width=100):
        """
            max_depth: maximum recursion depth to follow for each link
            max_width: maximum number of dict keys, i.e. width of tree
        """
        self.parser = Parser()
        self.start_url = start_url
        self.saver = Saver(savefile, max_width)
        self.max_depth = max_depth
        self.saver.starting_url(self.start_url)

    def start_scrapping(self, depth=0, start_url = None):
        if depth == self.max_depth:
            return
        if start_url == None:
            start_url = self.start_url
        nested_urls = self.get_urls(start_url)
        bool_break = self.save_data(start_url, nested_urls)
        if not bool_break:
            exit()

        if nested_urls == None:
            return
        else:
            for url in nested_urls:
                self.start_scrapping(depth+1, url)

    def get_urls(self, url):
        try:
            response = requests.get(url)
            web_page = response.content
            urls = self.parser.get_links(web_page)
        except requests.exceptions.RequestException as re:
            print(re)
            return
        return urls

    def save_data(self, start_url, nested_urls):
        reply = self.saver.save(start_url, nested_urls)
        if not reply:
            return False
        else:
            return True


class Parser:
    def get_links(self, html_doc):
        soup = BeautifulSoup(html_doc, 'html.parser')
        return [a['href'] for a in soup.find_all('a', href=True)]


