class solution:
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
    def bfs(adj):
        n=len(adj)
        visit=[0]*n
        ans=[]
        q=[0]
        visit[0]=True
        while q:
            i=q.pop(0)
            ans.append(i)
            for j in adj[i]:
                if not visit[j]:
                    visit[j]=True
                    q.append(j)
        return ans
s=solution()