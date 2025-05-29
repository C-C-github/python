def reverse(n,s):
    if n==0:
        return s
    return reverse(n//10,s*10+n%10)

n=int(input())
print(reverse(n,0))