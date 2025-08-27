# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4
def num(n):
    # def solve(n):
    #     if n==0:
    #         return 0
    #     mini=float('inf')
    #     i=1
    #     while i*i<=n:
    #         a=i*i
    #         mini=min(mini,1+solve(n-a))
    #         i+=1
    #     return mini
    # return solve(n)
    dp=[0]*(n+1)
    for i in range(1,n+1):
        mini=float('inf')
        for j in range(1,int(i**0.5)+1):
            a=j*j
            mini=min(mini,1+dp[i-a])
        dp[i]=mini
    return dp[n]
print(num(13))
        
        