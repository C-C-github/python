arr=[0,1,2]
r=0
for i in range(0,len(arr)):
    r=r^i^arr[i]
    print(f"r={r},i={i}")
r=r^len(arr)
print(r)