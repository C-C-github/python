def merge(arr,low,mid,high):
    l=low
    r=mid+1
    temp=[]
    while l<=mid and r<=high:
        if arr[l]<arr[r]:
            temp.append(arr[l])
            l+=1
        else:
            temp.append(arr[r])
            r+=1
    while l<=mid:
        temp.append(arr[l])
        l+=1
    while r<=high:
        temp.append(arr[r])
        r+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low]
        
    
def mergesort(arr,low,high):
    if low<high:
        mid=(low+high)//2
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)
    return arr
arr=[9,65,3,5,2,7,8]
print(mergesort(arr,0,len(arr)-1))