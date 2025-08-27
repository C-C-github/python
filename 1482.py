from typing import List
from bisect import bisect_left

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def check(days: int) -> bool:
            cnt = cur = 0
            for x in bloomDay:
                if x <= days:
                    cur += 1
                    if cur == k:
                        cnt += 1
                        cur = 0
                else:
                    cur = 0
            return cnt >= m

        left, right = min(bloomDay), max(bloomDay)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
