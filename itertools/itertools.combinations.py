import itertools
data = list(input().split())
string = data[0]
num = int(data[1])


for i in range(1,num+1):
        l =[]
        l = list(itertools.combinations(sorted(string),i))
        for i in l:
           print(*i,sep="")


