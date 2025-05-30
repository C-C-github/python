#input : 1 2 3 4 5 6 7
#output : [7, 1, 6, 2, 5, 3, 4]
def string(arr):
    arr.sort()
    l,r=0,len(arr)-1
    rlt=[]
    while l<=r:
        if r>=l:
            rlt.append(arr[r])
            r-=1
        if l<=r:
            rlt.append(arr[l])
            l+=1
    return rlt

arr=list(map(int,input().split()))
print(string(arr))