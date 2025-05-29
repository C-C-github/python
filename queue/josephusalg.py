#i=(i+k-1)%lengghtof list
def josephus(n,k):
    l=[i for i in range(1,n+1)]
    i=0
    while len(l)>1:
        i=(i+k-1)%len(l)
        l.pop(i)
    return l[0]

print(josephus(5,3))
print(josephus(5,2))