# implementatiion of an undirected graph using Adjacency Lists

"""
A: B, C, E (stored in node A)
B: A, C
C: A, B, D, E
D: C
E: A, C
"""


class Vertex:
    def __init__(self, n):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Adjacency_list:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    # add edge with vertices u and v
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neightbor(u)
            return True
        else:
            return False

    # print adjacency list
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
