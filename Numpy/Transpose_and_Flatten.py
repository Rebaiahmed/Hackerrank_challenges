import numpy
dim = list(input().strip().split(' '))
N = int(dim[0])
M = int(dim[1])
data =[]
data2=[]
for i in range(0,N):
    data.append(  list(   input().strip().split(' ')) )


for i in data :
    res = list(map(int,i))
    data2.append(res)

my_array = numpy.array(data2)
print (numpy.transpose(my_array))
print (my_array.flatten())

