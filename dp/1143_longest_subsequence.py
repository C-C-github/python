def longcommon(text1,text2):
    # def rec(t1,t2): # brute force for testing
    #     if t1=="" or t2=="":
    #         return 0
    #     if t1[0]==t2[0]:
    #         return 1+rec(t1[1:],t2[1:])
    #     else:
    #         return max(rec(t1,t2[1:]),rec(t1[1:],t2))
    # return rec(text1,text2)
    # m,n=len(text1),len(text2)
    # dp=[[0]*(n+1) for _ in range(m+1)]
    # for i in range(1,m+1):
    #     for j in range(1,n+1):
    #         if text1[i-1]==text2[j-1]:
    #             dp[i][j]=1+dp[i-1][j-1]
    #         else:
    #             dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # return dp[m][n]
    # memo={}
    # s1=text1
    # s2=text2
    # def dp(i,j):
    #     if i==len(s1) or j==len(s2):
    #         return 0
    #     if (i,j) in memo:
    #         return memo[(i,j)]
    #     if s1[i]==s2[j]:
    #         memo[(i,j)]=1+dp(i+1,j+1)
    #     else:
    #         memo[(i,j)]=max(dp(i+1,j),dp(i,j+1))
    #     return memo[(i,j)]
    # return dp(0,0)
    
    
print(longcommon("abc","abc"))