averages =[]
data = list(input().split())
X = int(data[0])
N= int(data[1])
for i in range(0,N):
    notes = map(float,input().split() )
    averages.append(notes)


for i in zip(*averages):
    print( sum(i)/len(i) )


