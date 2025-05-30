N,K,A = list(map(int,input().split()))

# b = N-A+1
# if b<=K:
#     print(K-b)
# else:
#     print(N-K+1)
ans = (A+K-1) % N
if ans == 0:
    print(N)
else:
    print(ans)