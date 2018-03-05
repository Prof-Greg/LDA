__author__ = 'greglakomski'

import numpy as np
import csv
import re

# Read in the saved Hellinger Data from file


combined_output_file_in = '/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/combined_output.csv'
savedfile = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/hellingerdata.txt"
target_to_peer_data_out = '/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/target_to_peer_data_out.csv'

newhellinger = np.loadtxt(savedfile)

writer = csv.writer(open(target_to_peer_data_out,'w+'),delimiter = ' ')


target_prov = "1740243245"
target_prov_type = ""

target_row = 0
peer_row = []


# first find row and type for target, then find all peer rows

with open(combined_output_file_in,'r') as f:
    reader = csv.reader(f, delimiter="%")
    rownum = 0
    for row in reader:
      rownum += 1
      if row[0] == target_prov:
        target_row = rownum
        row[1] = row[1].lstrip(' ')
        target_prov_type = row[1]
        break

    print(target_prov_type)

with open(combined_output_file_in,'r') as f:
    reader = csv.reader(f, delimiter="%")
    rownum = 0
    for row in reader:
      rownum += 1
      if row[1].lstrip(' ') == target_prov_type or row[1].lstrip(' ') == "Ophthalmology":
        peer_row.append(rownum)



# now analyze the hellinger data
# array is zero based

print len(peer_row)
print(peer_row)

hellinger_set = []
for i in range(0,len(peer_row)):
  print(newhellinger[target_row,peer_row[i]])
  hellinger_set.append(newhellinger[target_row,peer_row[i]])




# get rid of the zero associated with the target

hellinger_set.remove(0)
print(hellinger_set)

for i in hellinger_set:
  writer.writerow([i])

avg = reduce(lambda x,y:x+y,hellinger_set)/(len(peer_row)-1)

print(avg)
print(max(hellinger_set))
print(min(hellinger_set))




