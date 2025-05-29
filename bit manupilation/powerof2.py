def power(n):
    if n<=0:
        return False
    if n & (n-1)==0:
        return True
    return False
n=16
print(power(n))