__author__ = 'greglakomski'

import numpy as np
import csv
import re

# Read in the saved Theta Data from file
# The point if this code is to get all the theta rows for the target and its peers and save to file
# so that I can open it in R and make box plots


theta_file = '/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/model-final.theta'
savefile = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/common_theta.csv"


combined_output_file = '/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/combined_output.csv'


writer = csv.writer(open(savefile,'w+'),delimiter = ' ')


target_prov = "1740243245"
target_prov_type = ""

target_row = 0
peer_row = []


# first find row and type for target, then find all peer rows

with open(combined_output_file,'r') as f:
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


# added opthamologidts to optometrists

with open(combined_output_file,'r') as f:
    reader = csv.reader(f, delimiter="%")
    rownum = 0
    for row in reader:
      rownum += 1
      if row[1].lstrip(' ') == target_prov_type or row[1].lstrip(' ') == "Ophthalmology":
        peer_row.append(rownum)

print len(peer_row)
print(peer_row)

with open(theta_file,'r') as f:
    reader = csv.reader(f, delimiter=' ')
    rownum = 0
    for row in reader:
      rownum += 1
      if rownum in peer_row:
        writer.writerow(row)









