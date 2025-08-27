# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.
def uniquePaths(m, n):
    # dp = [[1] * n for _ in range(m)]
    # for i in range(1, m):
    #     for j in range(1, n):
    #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
    # return dp[m - 1][n - 1]
    # def rec(i,j):
    #     if i==0 or j==0:
    #         return 1
    #     left=rec(i,j-1)
    #     right=rec(i-1,j)
    #     return left+right
    # return rec(m-1,n-1)
    # dp=[[1]*n]*m
    # for i in range(1,m):
    #     for j in range(1,n):
    #         if i==0 or j==0:
    #             dp[i][j]=1
    #         elif i==0:
    #             dp[i][j]=dp[i-1][j]
    #         elif j==0:
    #             dp[i][j]=dp[i][j-1]
    #         else:
    #             dp[i][j]=dp[i-1][j]+dp[i][j-1]
    # return dp[m-1][n-1]
    # comb=[1]*n
    # for i in range(m-2,-1,-1):
    #     for j in range(n-2,-1,-1):
    #         comb[j]=comb[j]+comb[j+1]
    # return comb[0]
    arr1=[1]*n # most optimzed code o(root n)
    arr2=[1]*n
    for i in range(1,m):
        for j in range(1,n):
            arr2[j]=arr1[j]+arr2[j-1]
        arr1=arr2.copy()
    return arr1[n-1]
print(uniquePaths(50,30))