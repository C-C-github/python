def fib_dp(n):
    # if n==0:  # normal recusion method
        #     return 0
        # elif n==1 or n==2:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
        
        
    # dp = [0] * (n + 1) #Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space bootum up approach it is tabulation method
    # if n==0:
    #     dp[0]=0
    # else:
    #     dp[1]=1
    # for i in range(2, n + 1):
    #     dp[i] = dp[i - 1] + dp[i - 2]
    # return dp[n]
    
    
    # memo={} #Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space memoization like def fib(n,memo={}): for fast run time and compilation time faster.
    # if n in memo:
    #     return memo[n]
    # if n <=1:
    #     return n
    # else:
    #     memo[n] = fib_dp(n - 1) + fib_dp(n - 2)
    #     return memo[n]
    
    
    if n<=1:
        return 1
    else:
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
        return a
print(fib_dp(3))