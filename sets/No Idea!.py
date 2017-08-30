n,m = map(int, input().split())
l = list(map(int, input().split()))
A = set(map(int, input().split()))
B=set(map(int, input().split()))
happineis=0



for i in l :
  if( i in A):
    happineis+=1
  if(i in B):
       happineis-=1





print(happineis)
