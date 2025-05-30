def quick(arr,low,high):
    if low<high:
        p=low
        i=low
        j=high
        while i<j:
            while arr[i]<=arr[p] and i<high:
                i+=1
            while arr[j]>arr[p]:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[p],arr[j]=arr[j],arr[p]
        quick(arr,low,j-1)
        quick(arr,j+1,high)
    return arr

arr=list(map(int,input().split()))
print(quick(arr,0,len(arr)-1))