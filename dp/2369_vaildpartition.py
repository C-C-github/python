   
# def vaild(nums):
#     memo={}
#     def dfs(i):
#         if i==len(nums):
#             return True
#         if i in memo:
#             return memo[i]
#         ans=False
#         if i+1<len(nums) and nums[i]==nums[i+1]:
#             ans|=dfs(i+2)
#         if i+2<len(nums):
#             if nums[i]==nums[i+1]==nums[i+2]:
#                 ans|=dfs(i+3)
#             if nums[i+1]==nums[i]+1 and nums[i+2]==nums[i+1]+1:
#                 ans|=dfs(i+3)
#         memo[i]=ans
#         return ans
#     return dfs(0)

# nums = [4,4,4,5,6]
# print(valid(nums))  

# You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

# The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.
