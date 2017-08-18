def print_formatted(number):
    for i in range(1,number+1):
     print(i,oct(i)[2:],hex(i)[2:],bin(i)[2:],sep='  ', end='\n')




if __name__ == '__main__':

    n = int(input())
    print_formatted(n)


