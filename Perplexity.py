__author__ = 'greglakomski'

#calculates perplexity
# Note: Have to delete the first line in the wordmap before running this!!!!!!!!!!!!


import csv

from numpy import genfromtxt
# input the phi data as array

from math import log, exp

filepathin = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/EightyClustersStop/model-final.phi"

my_phi = genfromtxt(filepathin, delimiter=' ')

print(my_phi.shape)




filepathin2 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/EightyClustersStop/wordmap.txt"



# input the word list as array

# will need to use the word list to generate indexes

index_names = []


# create searchable list of words that matches the phi array
with open(filepathin2) as f2:
  reader2 = csv.reader(f2, delimiter = ' ')
  next(reader2)
  for row in reader2:
    index_names.append(row[0])



#import the Theta data for providers


filepathin3 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/EightyClustersStop/model-final.theta"

my_theta = genfromtxt(filepathin3, delimiter=' ')

print(my_theta.shape)

length_theta = my_theta.shape[1]

filepathin4 = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/code_array4.csv"

with open(filepathin4) as f4:
  line = list(f4)[0]
  linelist = line.split(' ')
  num_docs = linelist[0].replace('\r\n','')
  print('num docs',num_docs)


sum_words = 0
sum_log = 0

# Algorithm
for k in range(1,int(num_docs)):
#for k in range(1,3):

  with open(filepathin4) as f4:
    line = list(f4)[k]
    linelist = line.split(' ')
    #print(len(linelist))
    linelistset = set(linelist)

    sum_words += len(linelistset)

  p_w_d = 1

  for i in range (0,len(linelist)): # for every word in the document

    indexed_word = linelist[i].replace('\r\n','')

    word_index = index_names.index(indexed_word)
    #print(word_index)

    temp_sum = 0

    for j in range (0,length_theta): # for every topic

      #print(my_phi[j,word_index] * my_theta[k-1,j])

      temp_sum += my_phi[j,word_index] * my_theta[k-1,j] # k-1 because there is extra line in code array


  p_w_d *= temp_sum

  #print(p_w_d)

  log_p_w_d = log(p_w_d)

 # print('log pwd',log_p_w_d)

  sum_log += log_p_w_d

  print('sum_log',sum_log)

print('num words',sum_words)

perplex = exp(-sum_log/sum_words)

print(perplex)





