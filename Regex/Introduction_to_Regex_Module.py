import re
T = int(input())
results =[]
for i in range(0,T):
     N = input()
     results.append(bool(re.match(r"^[+-.]?[0-9]+\.[0-9]+$",N)))




for i in results:
    print(i)
