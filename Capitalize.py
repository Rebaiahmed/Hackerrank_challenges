def capitalize(string):
    list = string.split()
    #result =[]
    #for word in list:
         #word =word[0].upper() + word[1:]
         #result.append(word)


    return ' '.join((word.capitalize() for word in list))



if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
