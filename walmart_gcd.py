def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def operation(x,y):
    count=0
    while x>0 and y>0:
        g=gcd(x,y)
        x-=g
        y-=g
        count+=1
    return count
n,m=list(map(int,input().split()))
# res=n
# for i in range(len(n)):
#     res=gcd(res+i,n[i])
# print(res)
print(operation(n,m))
