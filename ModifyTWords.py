__author__ = 'greglakomski'
import csv

# generates the more user readable words and codes file.  Need to change filepaths for each experiment!

codehash = {}

filepath = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/codesummary.csv"
with open(filepath) as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:

      # create a hash table that just has the code and the short
      # description to use is post processing results
      codehash[row[0]]= row[1]



output = []
outputelement = []

filepath = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/FiveClustersStop/model-final.twords"

with open(filepath) as f:
    reader = csv.reader(f, delimiter=" ")
    for row in reader:
      line = row[0].strip(' \t\n')
      line2 = row[1].strip(' \t\n')
      if line != 'Topic':
        line = line.strip('[]')
        line = line.strip("''")
        line3 = row[3].strip(' \t\n')
        #print line
        #print(line +','+codehash[line])
        outputelement.append(line)
        if line in codehash:
          #print 'ok'
          outputelement.append(codehash[line])
          outputelement.append(line3)
        else:
          #print 'not ok'
          outputelement.append('CODE NOT FOUND')
        output.append(outputelement)
        outputelement= []
      else:
        #print('Topic'+ row[1])
        outputelement.append('Topic '+ line2)
        output.append(outputelement)
        outputelement= []


# write the annotated word
filepath = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/FiveClustersStop/words_and_codes.csv"



with open(filepath,'w') as f:
    writer = csv.writer(f, delimiter=',',quotechar=' ')
    for x in output:
      print(x)
      writer.writerow(x)









