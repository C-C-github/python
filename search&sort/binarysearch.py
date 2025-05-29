def binary_search(arr,tar):
    low=0
    last=len(arr)-1
    
    while low<=last:
        mid=(low+last)//2
        if arr[mid]==tar:
            return mid
        elif arr[mid]>tar:
            last=mid-1
        else:
            low=mid+1
    return -1
# arr=[1,2,3,4,5]
arr=list(map(int,input().split()))
n=700
# arr.sort()
# print(arr)
print(binary_search(arr,n))