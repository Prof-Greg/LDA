__author__ = 'greglakomski'

# cleans up the provider cross reference file to remove junk and normalize format

import csv
import re

filepath = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/provide_cross_ref3.csv"
filepathout = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/provide_cross_ref4.csv"
regex = re.compile('[^a-zA-Z ] ')

"add all the cleaning rules"

writer = csv.writer(open(filepathout,'w+'),delimiter = ' ')
with open(filepath) as f:
      reader = csv.reader(f, delimiter = ' ')
      for row in reader:
        row[2] = regex.sub('',row[2])
        row[2]= row[2].replace("INC",'')
        row[2]= row[2].replace(".",'')
        row[2]= row[2].replace("#",'')
        row[2]= row[2].rstrip()
        row[2]= row[2].lstrip()
        row[1]= row[1].replace('CRNA','Respiratory Nurse')

        writer.writerow(row)