import re
T = int(input().strip())
for i in range(0,T):
   try:
    s=input()
    re.compile(s)
    is_valid = True
   except re.error:
    is_valid = False
   print(is_valid)
