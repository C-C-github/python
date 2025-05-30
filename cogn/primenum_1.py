#array a ,n number addd prime numb locate even indices sequence.yout task open tresaure integer 
# the sum of all prime number locate even indices. input n=5,a=4,5,6,2,10 output 7 
def isprime(n):
    if n<=1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def prime_1index(n,a):
    sum1=0
    for i in range(1,n,2):
        if isprime(a[i]):
            sum1+=a[i]
    return sum1
    
n=int(input())
a=list(map(int,input().split()))
print(prime_1index(n,a))