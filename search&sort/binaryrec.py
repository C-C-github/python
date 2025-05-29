def binaryrec(arr,last,first,tar):
    mid=(last+first)//2
    if arr[mid]==tar:
        return mid
    elif arr[mid]>tar:
        return binaryrec(arr,mid-1,first,tar)
    else:
        return binaryrec(arr,last,mid+1,tar)
    
arr=list(map(int,input().split()))
n=int(input())
arr.sort()
print(arr)
print(binaryrec(arr,len(arr)-1,0,n))