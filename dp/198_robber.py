# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
def rob(nums): # recursive method
#     rob1, rob2 = 0, 0
#     for n in nums:
#         rob1, rob2 = rob2, max(rob1 + n, rob2)
#     return rob2

    # memo={}   #Using Top-Down DP (Memoization) - O(n^2) Time and O(n) Space memoization like def fib(n,memo={}): for fast run time and compilation time faster.
    # def dp(i):
    #     if i>=len(nums):
    #         return 0
    #     if i in memo:
    #         return memo[i]
    #     memo[i]=max(nums[i]+dp(i+2),dp(i+1))
    #     return memo[i]
    # return dp(0)
    
    
    dp=[0]*len(nums)  #Using Bottom-Up DP (Tabulation) - O(n^2) Time and O(n) Space bootum up approach it is tabulation method
    dp[0]=nums[0]
    for i in range(1,len(nums)):
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    return dp[-1]
    # space optimization
    
print(rob([2,7,9,3,1]))    
