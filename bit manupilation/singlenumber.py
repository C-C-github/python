def single(l):
    a,b=0,0
    for i in l:
        a=(a^i)&~b
        b=(b^i)&~a
    return a

l=list(map(int,input().split()))
print(single(l))