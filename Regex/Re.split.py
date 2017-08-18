import re
list =re.split("[,.]+",input())
for i in list :
    if(i.isdigit()):
      print(i)
