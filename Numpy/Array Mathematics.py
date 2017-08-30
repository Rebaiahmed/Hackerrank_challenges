import numpy
n,m = map(int, input().split())

l1 = [ list(map(int, input().split())) ]
l2 = [ list(map(int, input().split())) ]
a = numpy.array(l1, int)
b = numpy.array(l2, int)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print( a % b)
print(a**b)
