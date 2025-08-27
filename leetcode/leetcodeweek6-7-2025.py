class Solution(object):
    def minMoves(self, sx, sy, tx, ty):
        jandovrile=(sx,sy,tx,ty)
        if sx==tx and sy==ty:
            return 0
        x,y,moves=tx,ty,0
        while x>=sx and y>=sy:
            if x==sx and y==sy:
                return moves
            if x==y:
                if sx==0 and sy<=y:
                    x=0
                elif sy==0 and sx<=x:
                    y=0
                else:
                    return -1
                moves+=1
                continue
            if x>y:
                if x<2*y:
                    x-=y
                else:
                    if x%2!=0 or x//2<y:
                        return -1
                    x//=2
            else:
                if y<2*x:
                    y-=x
                else:
                    if y%2!=0 or y//2<x:
                        return -1
                    y//=2
            moves+=1
        return -1
a=Solution()

# Test cases
print(a.minMoves(1, 2, 5, 4))  # Output: 2
print(a.minMoves(0, 1, 2, 3))  # Output: 3
print(a.minMoves(1, 1, 2, 2))  # Output: -1





class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.components -= 1
        return True

class Solution:
    def minTimeToKComponents(self, n: int, edges: list[list[int]], k: int) -> int:
        if k == 1 or (not edges and k <= n):
            return 0

        edges.sort(key=lambda x: x[2])
        times = [0] + [e[2] for e in edges]

        def has_k_or_more_components(t):
            uf = UnionFind(n)
            for u, v, time in edges:
                if time > t:
                    uf.union(u, v)
            return uf.components >= k

        left, right = 0, len(times) - 1
        res = times[-1]

        while left <= right:
            mid = (left + right) // 2
            t = times[mid]
            if has_k_or_more_components(t):
                res = t
                right = mid - 1
            else:
                left = mid + 1

        return res

s = Solution()
print(s.minTimeToKComponents(2, [[0, 1, 3]], 2))           # Output: 3
print(s.minTimeToKComponents(3, [[0, 1, 2], [1, 2, 4]], 3)) # Output: 4
print(s.minTimeToKComponents(3, [[0, 2, 5]], 2))           # Output: 0




import heapq
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx

class Solution:
    def maintenanceCheck(self, c, connections, queries):
        uf = UnionFind(c)

        for u, v in connections:
            uf.union(u, v)

        # After all unions, compute final root for each node
        root_map = [uf.find(i) for i in range(c + 1)]

        # Heap for each component: stores online stations
        component_heap = defaultdict(list)
        online = [True] * (c + 1)

        for station in range(1, c + 1):
            heapq.heappush(component_heap[root_map[station]], 
                           station)

        result = []

        for query in queries:
            typ, x = query
            root = uf.find(x)

            if typ == 1:
                if online[x]:
                    result.append(x)
                else:
                    heap = component_heap[root]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    if heap:
                        result.append(heap[0])
                    else:
                        result.append(-1)
            else:
                online[x] = False

        return result


s = Solution()
print(s.maintenanceCheck(
    5,
    [[1,2],[2,3],[3,4],[4,5]],
    [[1,3],[2,1],[1,1],[2,2],[1,2]]
))
# Output: [3,2,3]

print(s.maintenanceCheck(
    3,
    [],
    [[1,1],[2,1],[1,1]]
))

#1. 
from typing import List

class Solution:
    def getValidCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        allowed_business = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        def is_valid_code(s):
            return s and all(c.isalnum() or c == '_' for c in s)

        valid_coupons = []
        for c, b, a in zip(code, businessLine, isActive):
            if is_valid_code(c) and b in allowed_business and a:
                valid_coupons.append((allowed_business[b], c))

        valid_coupons.sort()
        return [c for _, c in valid_coupons]


# Test cases
s = Solution()

# Test case 1
print(s.getValidCoupons(
    ["SAVE20", "", "PHARMA5", "SAVE@20"],
    ["restaurant", "grocery", "pharmacy", "restaurant"],
    [True, True, True, True]
))
# Expected Output: ["PHARMA5", "SAVE20"]

# Test case 2
print(s.getValidCoupons(
    ["GROCERY15", "ELECTRONICS_50", "DISCOUNT10"],
    ["grocery", "electronics", "invalid"],
    [False, True, True]
))
# Expected Output: ["ELECTRONICS_50"]
