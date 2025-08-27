edges=[
    ('A','B'),
    ('B','E'),
    ('A','C'),
    ('C','D'),
    ('D','D'),
    ('D','E'),
    ('D','A')
]
nodes=sorted({n for edge in edges for n in edge})
index_map={n:i for i,n in enumerate(nodes)}
size=len(nodes)
adj_matrix=[[0]*size for _ in range(size)]
for u,v in edges:
    i=index_map[u]
    j=index_map[v]
    adj_matrix[i][j]=1
print("Nodes:",nodes)
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)