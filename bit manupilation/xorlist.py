l=list(map(int,input().split()))
r=0
for i in l:
    r=r^i
    print(f"r={r},i={i}")
