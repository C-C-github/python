#[1 2 3 4 5 6] ouput:[1 4 2 5 3 6] first and last should same.middle all should be interleave
from collections import deque
def interleave(q):
    if len(q)%2!=0:
        return None
    stack=[]
    half=len(q)//2
    for _ in range(half):
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())
    for _ in range(half):
        q.append(q.popleft())
    for _ in range(half):
        stack.append(q.popleft()) #main list add middle of these [1 ----   6]
    while stack:
        q.append(stack.pop())
        q.append(q.popleft())

q=deque([1,2,3,4,5,6])
print("input:",list(q))
interleave(q)
print("output:",list(q))