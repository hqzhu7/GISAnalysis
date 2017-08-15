import csv
import os

#delete old file
os.remove("D:\Download\collision1.csv")

#create new file
f=open("D:\Download\collision1.csv",'w')
f.close()

#open a csv file
with open("D:\Download\collision.csv","rb") as input:
    reader= csv.reader( source )
    with open("D:\Download\collision1.csv","wb") as output:
        writer= csv.writer( output )
        for r in reader:
            wtr.writerow( (r[0], r[1], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10]) )
