def slice_method(n,knight):
    spl=0
    for i in range(n):
        ls=sum(1 for j in range(i) if knight[j]>knight[i])
        rs=sum(1 for j in range(i+1,n) if knight[j]>knight[i])
        if ls>rs:
            spl+=1
    return spl
n=int(input())
knight=list(map(int,input().split()))
print(slice_method(n,knight))