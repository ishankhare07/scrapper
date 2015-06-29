# scrapper
a scrapper written in python with urging requests and very BeautifulSoup

## Installing  
* Clone this repo  
```bash
$ git clone git@github.com:ishankhare07/scrapper.git && cd scrapper
```  
* Create a Virtual Environment, assuming python3  
```bash
$ pyvenv venv
$ source venv/bin/activate
```
* Install requirements from pip, (again assuming pip3 for python3)
```bash
$ pip3 install -r requirements.txt
```  

## Using the API
* Assuming python3 again  
```python
>>> from main import Scrapper
>>> s = Scrapper("http://news.ycombinator.com/","heacker_news")     #url, filename to store data
>>> s.start_scrapping()
```

* We can also issue recursion depths and max-urls to scan
```python
>>> from main import Scrapper
>>> s = Scrapper("http://news.ycombinator.com/",            #url
                "hacker_news",                              #filename to store data
                20,                                         #max-recursion depth
                30)                                         #max-urls to scan
>>> s.start_scrapping()
```

* Viewing the data
```python
>>> import shelve
>>> from pprint import pprint
>>> db = shelve.open('hacker_news')
>>> pprint(list(db.items()))
```
