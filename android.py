import csv
import matplotlib.pyplot as plt

##matplotlib plot to validate minimum version finding on 100000 to the whole dataset
with open('Google-playstore.csv','r', encoding='utf-8') as file:
    reader = csv.reader(file,delimiter=(','))
    apps=[]
    count=0
    for row in reader:
        count+=1
        if len(row[3])==3:
            apps.append(row)
android={}
for i in apps:
    if i[12] in android:
        android[i[12]]+=1
    else:
        android[i[12]]=1
ranges={}
for key in list(android.keys()):
    if key[(len(key)-2):len(key)]=='up':
        ranges[key]=android[key]

x=list(ranges.keys())
heights=list(ranges.values())
plt.figure(figsize=(12, 8))
plot=plt.bar(x, heights, width=0.8, bottom=None, align='center', data=None)
plt.xticks(x, rotation=90)
for bar in plot:
    plt.annotate(bar.get_height(), 
                 xy=(bar.get_x()+0.07, bar.get_height()+10), 
                     fontsize=8)

plt.show()
#App Name,App Id,Category,Rating,Rating Count,Installs,Minimum Installs,Maximum Installs,
#Free,Price,Currency,Size,Minimum Android,Developer Id,Developer Website,Developer Email,Released,
#Last Updated,Content Rating,Privacy Policy,Ad Supported,In App Purchases,Editors Choice,Scraped Time