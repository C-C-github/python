class Solution(object):
    def minimizedMaximum(self, n, quantities):
        def canDistribute(max_products):
            stores_needed = 0
            for q in quantities:
                stores_needed += (q + max_products - 1) // max_products
            return stores_needed <= n

        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1
        return left
