import re
S = input()
m = re.match(r'\d+',S)
print(m.groups())
