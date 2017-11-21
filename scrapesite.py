import os
import re
os.chdir('/Users/bricerandolph/Desktop/myrepos/scraping')
import scraper2
houzz = "https://www.houzz.com/professionals/architect/"
blob = scraper2.Scraper(houzz).scrape()
print(str(blob[0]))
print(re.findall('\d+', str(blob[0])))
