import csv,re,math

with open('googleplaystore.csv','r', encoding='utf-8') as file:
    reader = csv.reader(file,delimiter=(','))
    unfiltered=[]
    for row in reader:
        tempi=re.split(",", row[0])
        if len(row)==2:
            tempf=re.split(",", row[1])
            temp=tempi+tempf
        else:temp=tempi
        temp1=temp[0:5]
        temp2=temp[-2:len(temp)]
        temp=temp1+temp2
        unfiltered.append(temp)
    filtered=[]
    for i in unfiltered:
        if i[-1][-1]==";":
            filtered.append(i)
#App,Category,Rating,Reviews,Size,Current Ver,Android Ver
#Installs,Type,Price,Content Rating,Genres,Last Updated-----yet to be cleared

for i in filtered:
    if i[4][-1]=="k":
        i[4]=str(int(float(i[4][0:len(i[4])-1])*1000))
    if i[4][-1]=="M":
        i[4]=str(int(float(i[4][0:len(i[4])-1])*1000000))
    if not i[4].isnumeric() and i[4]!='Varies with device' and len(i[4])<4: 
        filtered.remove(i)

print(len(filtered))
filtered1=[]
for i in range(len(filtered)):
    if len(filtered[i][2])==3 and filtered[i][2]!='NaN':
        filtered1.append(filtered[i])

print(len(filtered1))
for i in filtered1:
    i[6]=i[6][0:(len(i[6])-1)]
    


header=['APP','CATEGORY','RATING','REVIEWS','SIZE','VERSION','ANDROID_VER']
with open('filtered.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    for i in filtered1:
        writer.writerow(i)