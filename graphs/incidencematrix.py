def crate_incidence(vertices,edges):
    v=len(vertices)
    e=len(edges)
    incidence_matrix=[[0]*e for _ in range(v)]
    vertex_index={vertex:i for i,vertex in enumerate(vertices)}
    for edge_index,(u,v) in enumerate(edges):
        u_index=vertex_index[u]
        v_index=vertex_index[v]
        incidence_matrix[u_index][edge_index]=1
        incidence_matrix[v_index][edge_index]=-1
    return incidence_matrix
def print_incidence(vertices,matrix):
    for v,row in zip(vertices,matrix):
        print(" " + " ".join(map(str,row)))

# | Node | e1 | e2 | e3 | e4 | e5 | e6 | e7 |
# | ---- | -- | -- | -- | -- | -- | -- | -- |
# | A    | 1  | 1  | 0  | 0  | 0  | 0  | 0  |
# | B    | 1  | 0  | 1  | 1  | 0  | 0  | 1  |
# | C    | 0  | 1  | 1  | 0  | 1  | 0  | 0  |
# | D    | 0  | 0  | 0  | 1  | 0  | 1  | 0  |
# | E    | 0  | 0  | 0  | 0  | 1  | 1  | 1  |
vertices=["A","B","C","D","E"]
edges=[("A","B"),("A","C"),("B","C"),("B","D"),("C","E"),("D","E"),("B","E")]
incidence_matrix=crate_incidence(vertices,edges)
print_incidence(vertices,incidence_matrix)