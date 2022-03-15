import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

with open('Google-playstore.csv','r', encoding='utf-8') as file:
    reader = csv.reader(file,delimiter=(','))
    apps=[]
    count=0
    for row in reader:
        count+=1
        if len(row[3])==3:
            apps.append(row)
######all fields in order######
#App Name,App Id,Category,Rating,Rating Count,Installs,Minimum Installs,Maximum Installs,
#Free,Price,Currency,Size,Minimum Android,Developer Id,Developer Website,Developer Email,Released,
#Last Updated,Content Rating,Privacy Policy,Ad Supported,In App Purchases,Editors Choice,Scraped Time

install_ranges={}
monetization=['Ads','purchases','Both Ads']
for i in apps:
    if i[5] in install_ranges:
        if i[20]=='False' and i[21]=='False':
            install_ranges[i[5]][0]+=1
        if i[20]=='True' and i[21]=='False':
            install_ranges[i[5]][1]+=1
        if i[20]=='False' and i[21]=='True':
            install_ranges[i[5]][2]+=1

        else:               
            install_ranges[i[5]][3]+=1
    else:
        install_ranges[i[5]]=[0,0,0,0]
        if i[20]=='False' and i[21]=='False':
            install_ranges[i[5]][0]=1
        if i[20]=='True' and i[21]=='False':
            install_ranges[i[5]][1]=1
        if i[20]=='False' and i[21]=='True':
            install_ranges[i[5]][2]=1
        else:               
            install_ranges[i[5]][3]=1


cat=list(install_ranges.keys())
heights=list(install_ranges.values())
both=[]
ads=[]
sales=[]
none=[]
for i in heights:
    none.append(i[0])
    ads.append(i[1])
    sales.append(i[2])
    both.append(i[3]) 
# create data
x = ['None', 'Both', 'Ads', 'Sales']
none = np.array(none)
both = np.array(both)
ads = np.array(ads)
sales = np.array(sales) 
# plot bars showing monetization across all install levels
figure(figsize=(10,12), dpi=80)
plt.bar(cat, none, color='r')
plt.bar(cat, both, bottom=none, color='b')
plt.bar(cat, ads, bottom=none+both, color='y')
plt.bar(cat, sales, bottom=none+both+ads, color='g')
plt.xticks(cat, rotation=90)
plt.xlabel("Installs")
plt.ylabel("Frequency")
plt.legend(x)
plt.title("Installs vs in-app monetization")

plt.savefig("Install-money_all.png")

