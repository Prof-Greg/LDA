__author__ = 'greglakomski'

import csv
print('start removing')

filepathin = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array2.csv"
filepathin3 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array3.csv"
filepathin2 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/provide_cross_ref2.csv"
filepathout = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array3.csv"
filepathout3 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array4.csv"
filepathout2 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/provide_cross_ref3.csv"





writer = csv.writer(open(filepathout,'w+'),delimiter = ' ')   # writes to code array 3

stops = ['G9008','A0425','99213','99214','97110','97140','98941']
empty_count = 0
rowindex = 0
startingnum = 0
emptyrows = []
def remove_stops(the_row,the_stop):
  return [value for value in the_row if value != the_stop]


with open(filepathin) as f:
  reader = csv.reader(f, delimiter = ' ')
  startingnum = int(next(reader)[0])
  write_count = 0

with open(filepathin) as f:
  reader = csv.reader(f, delimiter = ' ')
  for row in reader:
    rowindex +=1
    for stop in stops:
      row = remove_stops(row,stop)
    if row == []:
      empty_count += 1
      emptyrows.append(rowindex-1) # because there is no "number of records" in line 1 of provider dict
    else:
      writer.writerow(row)
      write_count += 1

# now that we have dropped records, need to change the number in line 1 of code_array
# I currently dont know how to write line 1 other than to go through the entire file

writer = csv.writer(open(filepathout3,'w+'),delimiter = ' ')  # writes to code array 4 which is final code array

rowindex = 0

with open(filepathin3) as f:
  reader = csv.reader(f, delimiter = ' ')
  for row in reader:
    rowindex +=1
    if rowindex == 1:
      row[0] = startingnum - empty_count
      writer.writerow(row)
    else:
      writer.writerow(row)



print('emptycount')
print(empty_count)

print(emptyrows)


writer = csv.writer(open(filepathout2,'w+'),delimiter = ' ')  # writes to cross reference 2 - final cross reference

rowindex = 0



with open(filepathin2) as f2:
  reader = csv.reader(f2, delimiter = ' ')
  for row in reader:
    rowindex +=1
    if rowindex not in emptyrows:
      writer.writerow(row)

print('finished with stop word removal')