import shelve

class Saver:
    def __init__(self, savefile, max_width):
        self.max_width = max_width
        self.file = shelve.open(savefile)

    def starting_url(self, url):
        self.file["starting url"] = url

    def save(self, url, url_list):
        num_keys = len(list(self.file.keys()))
        if num_keys == self.max_width:
            return False
        self.file[url] = url_list
        print("total keys=>", num_keys)
        return True
