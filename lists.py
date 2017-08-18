if __name__ == '__main__':
    N = int(input())
    List =[]
    for i in range(0,N):
      data = (input()).split()
      #12print(data[0])
      if(data[0]=="append"):
         List.append(int(data[1]))
      elif (data[0]=="remove"):
           List.remove(int(data[1]))
      elif(data[0]=="insert"):
           List.insert(int(data[1]),int(data[2]))
      elif(data[0]=="sort"):
           List.sort()
      elif (data[0]=="pop"):
          List.pop()
      elif(data[0]=="reverse"):
           List.reverse()
      else :
          print(List)





