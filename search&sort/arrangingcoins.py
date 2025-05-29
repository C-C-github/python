def coins(arr,n):
    l=0
    r=n
    while l<=r:
        mid=(l+r)//2
        tot=mid*(mid+1)//2
        if tot==n:
            return mid
        elif tot<n:
            l=mid+1
        else:
            r=mid-1            
    return r
arr=list(map(int,input().split()))
n=int(input())
print(coins(arr,n))