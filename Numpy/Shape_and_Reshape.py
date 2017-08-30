import numpy
arr = input().strip().split(' ')
newarr = numpy.array(arr,int)
newarr.shape = (3, 3)

print (numpy.reshape(newarr,(3,3)))
