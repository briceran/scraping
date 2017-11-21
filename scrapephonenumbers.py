import numpy as np
import pandas as pd
import scraper2 as sc
from collections import OrderedDict




blobs = []
numberlist = []
uniquenumbers = []
weblist = ['changeme1.com','changeme2.com']


#for every website in list, scrape html and save as blob
for i in weblist:
    blob = sc.Scraper(i).scrape()
    blobs.append(blob)

#grab all numbers
for blob in blobs:
        for item in blob:
            number = ''.join(re.findall('\d+', str(item)))
            numberlist.append(number)

len(numberlist)

unique = list(OrderedDict.fromkeys(numberlist))
len(unique)

#keep only numbers with 10 digits
for el in unique:
    if len(el)== 10:
        uniquenumbers.append(el)

len(uniquenumbers)
len(set(uniquenumbers))

# to save phone number list to csv
import csv

csvfile = "changeme.csv"

#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in uniquenumbers:
        writer.writerow([val])
