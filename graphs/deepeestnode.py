def dfs(adj):
    n=len(adj)
    visit=[0]*n
    ans=[]
    def solve(i):
        visit[i]=True
        ans.append(i)
        for j in adj[i]:
            if not visit[j]:
                solve(j)
    for i in range(n):
        if not visit[i]:
            solve(i)
    return ans
adj=[[1,2,3],
    [2,4,5],
    [3,-1,6],
    [4,-1,-1],
    [5,-1,-1],
    [6,-1,7],
    [7,-1,-1]]
dfs(adj)