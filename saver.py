import shelve

class Saver:
    def __init__(self, savefile):
        self.file = shelve.open(savefile)

    def starting_url(self, url):
        self.data["starting url"] = url

    def save(self, url, url_list):
        self.file[url] = url_list
