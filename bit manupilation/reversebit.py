r=0
n=5
for i in range(0,3):
    r=r<<1
    print(f"r={r},i={i}")
    r=r|(n&1)
    n=n>>1
    
print(r)