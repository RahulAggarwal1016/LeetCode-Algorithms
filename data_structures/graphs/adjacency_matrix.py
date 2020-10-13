# implementation of an undirected graph using Adjacency Matrix, with weighted or unwieghted edges
# Weighed Edges: Each edge (line connecting two nodes) has a value
# Directed: Each Node points/connects to others (one way -> no concept of "neighbors")

"""
  A B C D E 
A 0 1 1 0 1
B 1 0 1 0 0
C 1 1 0 1 1
D 0 0 1 0 0 
E 1 0 1 0 0
"""


class Vertex:
    def __init__(self, n):
        self.name = n


class Adjacency_Matrix:
    def __init__(self):
        # vertex dictionary
        self.vertices = {}
        # 2-dimensional array of edges (the matrix)
        self.edges = []
        # find index of any edge
        self.edge_indices = {}

    def add_vertex(self, vertex):
        # check if vertex is not in list and is of type vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            # add vertex to dictionary
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges) + 1))
            self.edges_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v + " ", end="")
            for j in range(len(self.edges)):
                print(self.edges[i][j], end="")
            print(" ")
