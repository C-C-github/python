def findMin(n,arr):
    arr.sort(reverse=True)
    print(arr)
    num1, num2=0,0
    for i in range(len(arr)):
        if i%2 == 0:
            num1 = num1*10 + arr[i]
        else:
            num2 = num2*10 + arr[i]
    return num1+num2

n = int(input())
arr = list(map(int,input().split()))
print(findMin(n,arr))