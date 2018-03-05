__author__ = 'greglakomski'
#computes the hellinger distance between two providers i,j for k thetas
# ran into a case where there were negative thetas so added abs to make sure it doesn't
# break the algorithm.
import numpy as np

from numpy import genfromtxt

from tempfile import TemporaryFile

import scipy.io

from math import sqrt, pow

filepathin = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/model-final.theta"

my_theta = genfromtxt(filepathin, delimiter=' ')

length_theta = my_theta.shape[0]
width_theta = my_theta.shape[1]

#length_theta = 5
#width_theta = 5


hellinger_dist = np.zeros((my_theta.shape[0],my_theta.shape[0]))

for i in range(0,length_theta):
  for j in range(0,length_theta):
    sum = 0
    for k in range(0,width_theta):
      temp = (pow((sqrt(abs(my_theta[i,k])) - sqrt(abs(my_theta[j,k]))),2))
      sum += temp
    print('i',i,'j',j)
    hellinger_dist[i,j] = 1/sqrt(2)* sqrt(sum)






np.savetxt(savefile,hellinger_dist,fmt='%-5.4f')


filepathout = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/hellinger.csv"

np.savetxt(
    filepathout,           # file name
    hellinger_dist,                # array to save
    fmt='%.4f',             # formatting, 2 digits in this case
    delimiter=' ',          # column delimiter
    newline='\n')           # new line character

savefile = "/Users/greglakomski/Desktop/GibbsLDA++-0.2/models/Medicare/TwentyClustersStop/hellingerdata.txt"
newhellinger = np.loadtxt(savefile)

shape(newhellinger)







