def search(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return -1

arr=list(map(int,input().split()))
n=int(input())
print(search(arr,n))