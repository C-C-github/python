def linear_rec(arr,tar):
    if arr[0]==tar:
        return 0
    else:
        return 1+linear_rec(arr[1:],tar)

arr=list(map(int,input().split()))
n=int(input())
print(linear_rec(arr,n))