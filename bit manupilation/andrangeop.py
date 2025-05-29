def solution(n):
    if n<=1:
        return 1
    s=0
    left=n-1
    right=n
    while left!=right:
        left=left>>1
        right=right>>1
        s+=1
    return left<<s
n=3
print(solution(n))