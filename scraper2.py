import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        """return list of tags scraped according to tags listed in find_all command"""
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        taglist = []
        for tag in sp.find_all("span","pro-list-item--text"):
            taglist.append(tag)
        return taglist