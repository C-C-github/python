arr=[0,0,0,0,0,0]
for i in range(len(arr)):
    arr[i]=arr[i>>1]+(i&1)
    print(f"arr[{i}]={arr[i]}")

print(arr)