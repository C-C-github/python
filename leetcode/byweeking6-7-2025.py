from math import gcd
from functools import reduce

def minimumStabilityFactor(nums, maxC):
    n = len(nums)
    bantorvixo = nums[:]
    if maxC >= n:
        return 0
    if maxC == 0:
        max_length = 0
        for i in range(n):
            current_gcd = nums[i]
            if current_gcd >= 2:
                max_length = max(max_length, 1)
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd >= 2:
                    max_length = max(max_length, j - i + 1)
                else:
                    break
        return max_length

    def is_feasible(k):
        intervals = []
        for i in range(n - k):
            sub = nums[i:i + k + 1]
            hcf = reduce(gcd, sub)
            if hcf >= 2:
                intervals.append((i, i + k))
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[1])
        changes = 0
        last_covered = -1
        for start, end in intervals:
            if start > last_covered:
                changes += 1
                last_covered = end
                if changes > maxC:
                    return False
        return True

    left, right = 0, n
    result = n
    while left <= right:
        mid = (left + right) // 2
        if is_feasible(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    if result == 0:
        count_stable = sum(1 for x in nums if x >= 2)
        if count_stable > maxC:
            return 1
        return 0
    return result


# Test cases
print(minimumStabilityFactor([1035,1684,1830,1113,2988,2440,3518,4044,2550,2730,2977,2608,3197,214,3882,283], 2))# Output: 2
print(minimumStabilityFactor([14, 2, 22], 1))   # Output: 1
print(minimumStabilityFactor([3, 5, 10], 1))    # Output: 1
print(minimumStabilityFactor([2, 6, 8], 2))     # Output: 1
print(minimumStabilityFactor([2, 4, 9, 6], 1))  # Output: 2


# import heapq
# from collections import defaultdict
# from typing import List  # ✅ Fix 2: Add this

# class Solution:
#     def minTime(self, n: int, edges: List[List[int]]) -> int:
#         dalmu = defaultdict(list)
#         for u, v, start, end in edges:
#             dalmu[u].append((v, start, end))
        
#         min_time = [float('inf')] * n
#         min_time[0] = 0
#         heap = [(0, 0)]
        
#         while heap:
#             t, u = heapq.heappop(heap)
#             if u == n - 1:
#                 return t
#             if t > min_time[u]:
#                 continue
#             for v, s, e in dalmu[u]:
#                 if t > e:
#                     continue
#                 arrive = max(t, s) + 1  # ✅ Fix 1: Proper indentation
#                 if arrive < min_time[v]:
#                     min_time[v] = arrive
#                     heapq.heappush(heap, (arrive, v))
        
#         return -1

# a=Solution()
# print(a.minTime(3,[[0,1,0,1],[1,2,2,5]]))
# class Solution:
#     def minimumCost(self, m: int, n: int, waitCost: list[list[int]]) -> int:
#         cache = {}

#         def solve(i: int, j: int, parity: int) -> int:
#             if i >= m or j >= n:
#                 return float('inf')
#             if i == m - 1 and j == n - 1:
#                 return (i + 1) * (j + 1)

#             key = (i, j, parity)
#             if key in cache:
#                 return cache[key]

#             if parity == 1:  # move step
#                 move_cost = (i + 1) * (j + 1)
#                 res = move_cost + min(
#                     solve(i + 1, j, 0),
#                     solve(i, j + 1, 0)
#                 )
#             else:  # wait step
#                 res = waitCost[i][j] + solve(i, j, 1)

#             cache[key] = res
#             return res

#         return solve(0, 0, 1)




# s = Solution()
# print(s.minimumCost(1, 2, [[1, 2]]))             # 3
# print(s.minimumCost(2, 2, [[3, 5], [2, 4]]))     # 9
# print(s.minimumCost(2, 3, [[6,1,4],[3,2,5]]))    # 16
# print(s.minimumCost(2, 1, [[1], [2]]))           # 4



# class Solution(object):
#     def concatHex36(self, n):
#         """
#         :type n: int
#         :rtype: str
#         """
#         def convert(num, base):
#             digits = []
#             while num:
#                 rem = num % base
#                 digits.append(chr(rem + 48) if rem < 10 else chr(rem - 10 + 65))
#                 num //= base
#             return ''.join(reversed(digits)) if digits else "0"

#         return convert(n * n, 16) + convert(n * n * n, 36)
# s=Solution()
# print(s.concatHex36(36))

