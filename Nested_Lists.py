if __name__ == '__main__':
    List =[]
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    marksheet.sort(key=lambda x: x[1])

    print(marksheet)
