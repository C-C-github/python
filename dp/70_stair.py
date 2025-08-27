# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
def climb(n):
    # if n == 1: # recusive method
    #     return 1
    # if n == 2:
    #     return 2
    # return climb(n-1)+climb(n-2)
    
    # if n<=2:   # manula recusive
    #     return n
    # else:
    #     a,b=1,2
    #     for i in range(3,n+1):
    #         a,b=b,a+b
    #     return b
    # if n<3: #Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space bootum up approach it is tabulation method
    #     return n
    # dp=[0]*(n+1)
    # dp[1]=1
    # dp[2]=2
    # for i in range(3,n+1):
    #     dp[i]=dp[i-1]+dp[i-2]
    # return dp[n]
    memo={}   #Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space memoization like def fib(n,memo={}): for fast run time and compilation time faster.
    if n in memo:
        return memo[n]
    if n<3:
        return n
    memo[n]=climb(n-1)+climb(n-2)
    return memo[n]

print(climb(1))