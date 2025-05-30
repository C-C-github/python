# input 1 2 3 4 5 6 ouput 3. return the first element
def clock(n,arr):
    k=0
    num=0
    while(k<=(n//2)):
        k+=1
        arr=[arr[n-1]]+arr[0:n-1]
        num=num*10+arr[n-k]
        arr.remove(arr[n-k])
        n=n-1
    print("Number : ",num)
    return arr
        
    # return arr[n//2-1]
arr=list(map(int,input().split()))
n=len(arr)
arr=clock(n,arr)
for i in range(len(arr)):
    print(arr[i],end=f": index {i+1} ")
print("\nfirst number:",arr[0])