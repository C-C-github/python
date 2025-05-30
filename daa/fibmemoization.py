def Fibo(n, memo={}):
    if n ==0 or n==1:
        return n
    if not n in memo:
        memo[n] = Fibo(n-1,memo) + Fibo(n-2,memo)
    return memo[n]
print(Fibo(3))