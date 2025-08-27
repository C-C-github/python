def printone(n):
    if n == 0:
        return
    print(n)
    printone(n-1)

n = int(input())
printone(n)