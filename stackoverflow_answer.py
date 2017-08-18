
if __name__ == '__main__':
    names =[]
    numbers =[]
    print ("enter the name with number")
    for i in range(0,2):
         print("enter the name order "+ (i+1))
         data = input().split(' ')
         numbers.append(data[1])
         names.append(data[0])

    for i in range(0,2):

         print("name " + names[i] + "number" + numbers[i])


    print("enter the name to earch ")
    name = input()
    found = name in names
    if(found):
        print(numbers[names.index(name)])

    else :
        print("Name Not Found")



