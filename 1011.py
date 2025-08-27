from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            cmt = 1
            ws= 0
            for w in weights:
                if ws + w > capacity:
                    cmt += 1
                    ws = 0
                ws += w
            return cmt <= days

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if can_ship(mid):
                high = mid
            else:
                low = mid + 1
        return low
s=Solution()

print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))