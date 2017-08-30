import numpy
arr = list(map(int,input().strip().split(' ')))
data1 =[]
data2 =[]



for i in range(0,arr[0]):
      data1.append(  list(map(int,input().strip().split(' ')) ))


for i in range(0,arr[1]):
      data2.append(   list( map(int,input().strip().split(' ')) ))






array_1 = numpy.array(data1)
array_2 = numpy.array(data2)

print (numpy.concatenate((array_1, array_2)) )




