N = int(input())
arr = []
notes =[]

for i in range(0,N):
    name = input()
    note = float(input())
    notes.append(note)
    arr.append([name,note])




for x in arr :
    if(x[1]==notes[1]):
        print(x[0])



