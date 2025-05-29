def binarysearch(arr,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
def exponentialsearch(arr,key):
    if arr[0]==key:
        return 0
    i=1
    while i<len(arr) and arr[i]<=key:
        i=i*2
    return binarysearch(arr,i//2,min(i,len(arr)-1),key)

arr=list(map(int,input().split()))
arr.sort()
n=int(input())
print(arr)
print(exponentialsearch(arr,n))