def interpolation_search(array,value):
    low=0
    high=len(array)-1
    while low<=high and value>=array[low] and value<=array[high]:
        mid=low+((value-array[low])*(high-low)//(array[high]-array[low]))
        if array[mid]==value:
            return mid
        elif array[mid]<value:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=list(map(int,input().split()))
n=int(input())
arr.sort()
print(arr)
print(interpolation_search(arr,n))