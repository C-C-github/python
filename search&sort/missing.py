def missing(num):
    n=len(num)
    tot=n*(n+1)//2
    return tot-sum(num)

num=list(map(int,input().split()))
print(missing(num))