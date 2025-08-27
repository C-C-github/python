# def processString(s: str) -> str:
#     result = []

#     for ch in s:
#         if 'a' <= ch <= 'z':
#             result.append(ch)
#         elif ch == '*':
#             if result:
#                 result.pop()
#         elif ch == '#':
#             result += result
#         elif ch == '%':
#             result.reverse()

#     return ''.join(result)


# print(processString("a#b%*"))  # Output: "ba"
# print(processString("z*#"))    # Output: ""


# class Solution(object):
#     def minCost(self, n, edges, k):
#         parent = list(range(n))

#         def find(x):
#             while parent[x] != x:
#                 parent[x] = parent[parent[x]]
#                 x = parent[x]
#             return x

#         def union(x, y):
#             px, py = find(x), find(y)
#             if px == py:
#                 return False
#             parent[py] = px
#             return True

#         edges.sort(key=lambda x: x[2])
#         mst_weights = []

#         for u, v, w in edges:
#             if union(u, v):
#                 mst_weights.append(w)
#                 if len(mst_weights) == n - 1:
#                     break

#         mst_weights.sort(reverse=True)

#         for _ in range(k - 1):
#             if mst_weights:
#                 mst_weights.pop(0)

#         return max(mst_weights) if mst_weights else 0
# sol = Solution()
# print(sol.minCost(5, [[0,1,4],[1,2,3],[1,3,2],[3,4,6]], 2))  # Output: 4
# print(sol.minCost(4, [[0,1,5],[1,2,5],[2,3,5]], 1))          # Output: 5


# def get_kth_character(s, k):
#     ops = []
#     length = 0

#     for c in s:
#         if c.islower():
#             ops.append((c, length))
#             length += 1
#         elif c == '*':
#             if length > 0:
#                 length -= 1
#                 ops.append(('*', length))
#         elif c == '#':
#             ops.append(('#', length))
#             length *= 2
#         elif c == '%':
#             ops.append(('%', length))

#         if length > 10**15:
#             break

#     def find_char(k, ops, length):
#         for i in reversed(range(len(ops))):
#             op, l = ops[i]
#             if k >= length:
#                 return '.'
#             if op.islower():
#                 if k == length - 1:
#                     return op
#                 length -= 1
#             elif op == '*':
#                 length += 1
#                 if k == length - 1:
#                     return '.'
#             elif op == '#':
#                 half = length // 2
#                 if k >= half:
#                     k -= half
#                 length = half
#             elif op == '%':
#                 k = length - 1 - k
#         return '.'

#     return find_char(k, ops, length)

# print(get_kth_character("a#b%*", 1))     # Output: "a"
# print(get_kth_character("cd%#*#", 3))    # Output: "d"
# print(get_kth_character("z*#", 0))       # Output: "."

def longestPalindromePath(n, edges, label):
    mervanqilo = {'n': n, 'edges': edges, 'label': label}
    graph = [0] * n
    for u, v in edges:
        graph[u] |= 1 << v
        graph[v] |= 1 << u
    char_bits = {}
    for i, ch in enumerate(label):
        if ch not in char_bits:
            char_bits[ch] = 0
        char_bits[ch] |= 1 << i
    visited = set()
    answer = [0]  # use list to allow mutation inside dfs
    def dfs(a, b, mask):
        state = (mask << 8) | (a << 4) | b
        if state in visited:
            return
        visited.add(state)
        length = bin(mask).count('1')
        if length > answer[0]:
            answer[0] = length
        max_possible = length + ((n - length) // 2) * 2
        if max_possible <= answer[0]:
            return
        def dfs_helper(x_bits, y_bits):
            if not x_bits:
                return
            bit_i = x_bits & -x_bits
            i = bit_i.bit_length() - 1
            compatible = y_bits & char_bits.get(label[i], 0)
            comp = compatible
            while comp:
                bit_j = comp & -comp
                j = bit_j.bit_length() - 1
                if i != j:
                    dfs(i, j, mask | bit_i | bit_j)
                comp ^= bit_j
            dfs_helper(x_bits ^ bit_i, y_bits)
        dfs_helper(graph[a] & ~mask, graph[b] & ~mask)
    for i in range(n):
        dfs(i, i, 1 << i)
    for u, v in edges:
        if label[u] == label[v]:
            pair_mask = (1 << u) | (1 << v)
            dfs(u, v, pair_mask)
    return answer[0]



print(longestPalindromePath(3, [[2,0],[2,1]], "mll"))   # Output: 3
print(longestPalindromePath(3, [[0,1],[0,2]], "abc"))   # Output: 1
print(longestPalindromePath(4, [[0,2],[0,3],[3,1]], "bbac")) # Output: 3
