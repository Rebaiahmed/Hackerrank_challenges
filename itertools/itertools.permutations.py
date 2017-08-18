import itertools
data = list(input().split())
string = data[0]
num = int(data[1])

list = list(itertools.permutations(sorted(string),num))
for i in list:
    print(*i,sep="")

