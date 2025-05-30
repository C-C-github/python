#house robber you cannot roob two adjecent houses.
# def rob(nums):
    #o(n powe2) solution
    # l=len(nums)
    # dp=[0]*l
    # dp[0]=nums[0]
    # dp[1]=max(nums[0],nums[1])
    # for i in range(2,l):
    #     dp[i]=max(dp[i-1],dp[i-2]+nums[i])
    #     print(dp)
    # return dp[l-1]

    #o(n) solution
    # if not nums:
    #     return 0
    # if len(nums)==1:
    #     return nums[0]
    # prev2,prev1=0,nums[0]
    # for i in range(1,len(nums)):
    #     curr=max(prev1,prev2+nums[i])
    #     prev2=prev1
    #     prev1=curr
    #     print(f'prev2:{prev2},prev1:{prev1}={curr}')
    # return prev1
def maxi(nums):
    f=g=0
    for x in nums:
        f,g=max(f,g),f+x
        print(f'x:{x},f:{f},g:{g}')
    return max(f,g)
            
def rob(nums):
        if len(nums)==1:
            return nums[0]
        return max(maxi(nums[1:]),maxi(nums[:-1]))
nums=[1,2,3,1]
print(rob(nums))