# input 0 1 3 50 75 ,lower 0 ,upper 99. output: [[2,2],[4,49],[51,74],[76,99]]
def shortest_sort_missing(arr,lower,upper):
    arr.sort()
    res=[]
    for i in arr:
        if lower<i:
            res.append([lower,i-1])
        lower=i+1 
        print("loop: ",res)
    if lower<=upper:
        res.append([lower,upper])
    return res
arr=list(map(int,input().split()))
lower=int(input())
upper=int(input())
print("The ranges: ",shortest_sort_missing(arr,lower,upper))