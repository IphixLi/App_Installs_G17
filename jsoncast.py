from ftplib import all_errors
from pprint import pprint
import json,csv

#convert poorly formatted csv file into JSON file for tableau use.
with open('Google-playstore.csv','r', encoding='utf-8') as file:
    reader = csv.reader(file,delimiter=(','))
    count=0
    track=0
    keys=['App Name', 'App Id', 'Category', 'Rating',
    'Rating Count', 'Installs', 'Minimum Installs', 'Maximum Installs',
     'Free', 'Price', 'Currency', 'Size', 'Minimum Android', 'Developer Id', 
     'Developer Website', 'Developer Email', 'Released', 'Last Updated',
      'Content Rating', 'Privacy Policy', 'Ad Supported', 'In App Purchases', 
      'Editors Choice', 'Scraped Time']
    all=[]
    size=[]
    installs=[]
    entries=[]
    for i in reader:
        if count==0:
            keys=i
            count+=1
        else:                                     
            if track<=200000:
                entries.append(i)
                track+=1

for i in entries:
   data={}
   for j in range(len(keys)):
        data[keys[j]]=i[j]
   JSoned=json.dumps(data)
   format=JSoned+","
   print(format)

##pipe this to a separate json file as python3 jsoncast.py >tableau.json