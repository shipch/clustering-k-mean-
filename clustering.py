from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten

import matplotlib.pyplot as plt
import csv

import numpy as np


K = 3
value_arr = []
country_name_arr = []
a=0
b=0
count = 0


with open('working-hours-per-week.csv' , 'rb') as hour:
        data = csv.reader(hour)
        data = [row for row in data]
        for row in data:
            a=a+1
            if row[2] not in (None, ""):
                if int(row[1]) == 2006:
                    value_arr.append([float(x) for x in row[2:]])
                    country_name_arr.append([row[0]])


print a
print b



data = vstack( value_arr )
country_name = vstack(country_name_arr)

data = whiten(data)

centroids, distortion = kmeans(data,3)

yaxis=[]


idx,_ = vq(data,centroids)

#plot(data[idx==0,0], data[idx==0,1],'ob',data[idx==1,0], data[idx==1,1],'or',data[idx==2,0], data[idx==2,1],'og')

for i in range(K):
    result_names = country_name[idx==i, 0]
    result_value = data[idx==i,0]
    print "//////////////////////////////////////////////////////////////"
    print "CLUSTER " + str(i+1)
    print "Centroid = " + str(centroids[i-1][0])
    print ".........................................."
    n = 0
    yaxis = []
    for name in result_names:
        yaxis.append(float(result_value[n]/centroids[i-1][0]))
        print name + ' : ' + str(result_value[n])
        n = n+1
    plt.scatter(result_value,yaxis,label='cluster'+str(i+1),color='m')





plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
