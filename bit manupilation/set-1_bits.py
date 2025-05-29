def set1(n):
    c=0
    for i in n:
        c+=i&1
        i>>=1
    return c
n=[12,6,9,8,1]
print(set1(n))