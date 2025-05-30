# input:  3 5 2 1 6 4
#output: [1, 3, 2, 5, 4, 6]
def wiggle(arr1):
    arr1.sort()
    for i in range(1,len(arr1)-1,2):
        arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
    return arr1
arr1=list(map(int,input().split()))
print(wiggle(arr1))
