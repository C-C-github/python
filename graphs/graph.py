edges={
    ('A','B'),
    ('A','C'),
    ('B','D'),
    ('C','D'),
    ('D','E'),
    ('D','D')
}
graph={}
for u,v in edges:
    if u==v:
        graph[u]=[]
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
    graph[u].append(v)
    graph[v].append(u)
for n in graph:
    print(n,':',graph[n])