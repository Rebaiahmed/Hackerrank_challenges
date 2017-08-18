T = int(input().strip())
for i in range(0,T):
    try:
     l = list(input().split())
     a = int(l[0])
     b = l[1]
     print(a//int(b))
    except ValueError as e:
     print ("Error Code:",e)
     continue
    except ZeroDivisionError:
     print("Error Code: integer division or modulo by zero")
     continue

