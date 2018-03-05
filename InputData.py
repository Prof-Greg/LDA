__author__ = 'greglakomski'

import csv
import time
#from CombineOutput.py import combine

codes_dict = dict()
provider_dict = dict()

start = time.time()

linenumber = 0

# This takes the Fraud data and looks at each line
# If the line is from a provider classified as one of several classes
# then we add the provider code to the codes_dict as the key if not already there
# Then we add the code for that line item to the dict as a value for that key
#
filepath = "/Volumes/USB DISK/Medicare/AllMedicareFraudData.txt"
print('start')
with open(filepath) as f:
    reader = csv.reader(f, delimiter="\t")


    rownum = 0


    for row in reader:
      if rownum > 1:
        # I am only interested in certain types of providers, so we need to
        # check that field.

        # Limit to Vermont
        if (row[11] == 'VT'):

          #if the provider code is in the code dictionary, don't add another key
          #just go ahead and add the care code into the dictionary
          # modified to add the care code the number of times the doctor
          # actually billed the code
          if int(row[0]) in codes_dict:
            temp =[]
            temp = [str(row[16]) for i in range(int(float(row[18])))]
            codes_dict[int(row[0])].extend(temp)
            temp = []

          else:
            #if there is no key
            # print("key not present")
            #print("in rownum"+ repr(rownum))
            temp =[]
            temp = [str(row[16]) for i in range(int(float(row[18])))]
            codes_dict[int(row[0])]=temp
            linenumber += 1 # counts number of records
            temp = []

          if int(row[0]) in provider_dict:
            pass
          else:
            # 1003007741:'Family Practice','DEPPEN','WA',  <- sample
            provider_dict[int(row[0])] = [(row[13])]
            provider_dict[int(row[0])].append((row[1]))
            provider_dict[int(row[0])].append((row[11]))
            #print(row[13])
            #print(row[1])
            #print(row[11])
            #print(row[18])

        else:
          pass

      rownum += 1


      #9153274:
      if rownum > 9153274:
        #print(maxlength)
      #if rownum > 200000:
        break


print('Start length analysis')
# Based on a length criteria, identify providers and put the ids in a list
# This removed  providers that were hospitals and did not break out individual doctors

dlist = [] # the list
txt = ''
code_count = 0
max_length = 0
for x in codes_dict:
  for codes in codes_dict[x]:
    code_count +=1
  if code_count > 50000:
    print('code count',code_count)
    print(x)
    dlist.append(x)
  if code_count < 50000:
    if code_count > max_length:
      max_length = code_count
  code_count = 0

#print(dlist)

print(max_length)



#  This code removes the providers in the dlist from the dicts
codes_dict = {i:codes_dict[i] for i in codes_dict if i not in dlist}
provider_dict = {i:provider_dict[i] for i in provider_dict if i not in dlist}
linenumber = linenumber - len(dlist)



'''
# look at the final codes_dict
txt = ''
print("start print")
#print(codes_dict)
for x in codes_dict:
  txt = ''
  for codes in codes_dict[x]:
    txt += repr(codes) + ","
  print(repr(x) + ":"+ txt)
  #print(repr(x) + ":"+ codes)
'''
'''
# look at the final provider_dict
txt = ''
print("start print")
#print(codes_dict.)
for x in provider_dict:
  txt = ''
  for items in provider_dict[x]:
    txt += repr(items) + ","
  print(repr(x) + ":"+ txt)
    #print(repr(x) + ":"+ codes)

'''

print("linenumber",linenumber) # number of records


# Write the codes array (values) to a file for processing by collapsed Gibbs
with open("/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array2.csv", "wb") as f:
    writer = csv.writer(f, delimiter = ' ')
    line1 = []
    linenumber = [linenumber]
    writer.writerow(linenumber)

    for x in codes_dict:
      writer.writerow(codes_dict[x])


# Write the codes array (values) to a file for import into R
with open("/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_arrayR2.csv", "wb") as f:
    writer = csv.writer(f, delimiter = ' ')
    line1 = []   # not sure why I need to do this
    for i in range(0,max_length):
      line1.append('A')
    writer. writerow(line1)
    linenumber = [linenumber]
    writer.writerow(linenumber)

    for x in codes_dict:
      writer.writerow(codes_dict[x])

# Write the provider cross reference (values) to a file for processing by collapsed Gibbs
with open("/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/provide_cross_ref2.csv", "wb") as f:
    writer = csv.writer(f, delimiter = ' ')

    for x in provider_dict:

        provider_dict[x].insert(0,x)
        writer.writerow(provider_dict[x])


#combine()

end = time.time()





# Write the dictionary to a file so we can also get provider type and info associated into a file


elapsed = end - start
print "Time taken: ", elapsed, "seconds."

