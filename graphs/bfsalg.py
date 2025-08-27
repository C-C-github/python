from collections import deque
def bfs(graph,start):
    visted=set()
    queue=deque([start])
    visted.add(start)
    while queue:
        vertex=queue.popleft()
        print(vertex,end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visted:
                visted.add(neighbour)
                queue.append(neighbour)
             
abj={
    "A":["B","C"],
    "B":["D","E"],
    "C":["F"],
    "D":[],
    "E":["F"],
    "F":[]
}
bfs(abj,"B")
# def insert(edges):
#     graph = {}
#     for u, v in edges:
#         if u not in graph:
#             graph[u] = []
#         if v not in graph:
#             graph[v] = []
#         graph[u].append(v) 
#     return graph               
# graph={
#     ("A","B"),
#     ("B","C"),
#     ("C","E"),
#     ("E","D"),
#     ("D","E"),
#     ("E","F"),
#     ("F","G"),
#     ("G",'F'),
#     ("F",'E'),
#     ("E","C"),
#     ("C","B"),
#     ("B","A")   
# }

# abj=insert(graph)