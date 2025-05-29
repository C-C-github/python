# cities = ["New York", "Los Angeles", "Chicago"]
# temperatures = [75, 85, 68]
# for city, temp in zip(cities, temperatures):
#     print(f"{city} has a temperature of {temp}°F.")
# # Expected output:
# # New York has a temperature of 75°F.
# # Los Angeles has a temperature of 85°F.
# # Chicago has a temperature of 68°F.


# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# s="aa"
# p="*"
# for i in range(len(s)-len(p)+1):
#     c=0
# if s[i:i+len(p)]!=p:
#         print(True)
# else:
#         print(False)


# You are given integers n, m, and k.

# There are two logs of lengths n and m units, which need to be transported in three trucks where each truck can carry one log with length at most k units.

# You may cut the logs into smaller pieces, where the cost of cutting a log of length x into logs of length len1 and len2 is cost = len1 * len2 such that len1 + len2 = x.

# Return the minimum total cost to distribute the logs onto the trucks. If the logs don't need to be cut, the total cost is 0.

#  

# Example 1:

# Input: n = 6, m = 5, k = 5

# Output: 5

# Explanation:

# Cut the log with length 6 into logs with length 1 and 5, at a cost equal to 1 * 5 == 5. Now the three logs of length 1, 5, and 5 can fit in one truck each.

# Example 2:

# Input: n = 4, m = 4, k = 6

# Output: 0

# Explanation:

# The two logs can fit in the trucks already, hence we don't need to cut the logs.

#  

# Constraints:

# 2 <= k <= 105
# 1 <= n, m <= 2 * k
# The input is generated such that it is always possible to transport the logs.©leetcode

class Solution(object):
    def minCuttingCost(self, n, m, k):
        from functools import lru_cache

        @lru_cache(None)
        def min_cost(x):
            if x <= k:
                return 0
            res = float('inf')
            for i in range(1, x):
                res = min(res, i * (x - i) + min_cost(i) + min_cost(x - i))
            return res

        return min_cost(n) + min_cost(m)

            
s=Solution()
print(s.minCuttingCost(6,5,5))