import itertools
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
list = list(itertools.product(A,B) )
for i in list :
     print(i,end=' ')


