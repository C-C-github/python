# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
def ins(s):
    dp=[[0]*(len(s)+1) for _ in range(len(s)+1)]
    rev=s[::-1]
    n=len(s)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]==rev[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return n-dp[n][n]

print(ins("leetcode"))