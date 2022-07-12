# Class to represent graph and all the functions
class Graph:
    """ Constructor """

    def __init__(self, vertex):

        self.V = vertex
        self.exist = False
        self.edgeList = []  # List to store all edges in the graph
        self.Node = ["GLA", "BDX", "MB", "KL", "MVD"]  # Store all vertices in a list
        self.adjList = {}  # Dictionary to represent adjacency list

        for node in self.Node:
            self.adjList[node] = {}  # Create dictionary for each vertex

        self.adjList['GLA']['BDX'] = 1254  # Default graph
        self.adjList['MB']['BDX'] = 7240
        self.adjList['MB']['KL'] = 3599
        self.adjList['MVD']['GLA'] = 11225
        self.adjList['MVD']['KL'] = 15812
        self.adjList['BDX']['MB'] = 7240
        self.adjList['KL']['MVD'] = 15812
        self.adjList['BDX']['GLA'] = 1254
        self.adjList['KL']['MB'] = 3599
        self.adjList['GLA']['MVD'] = 111225
    
    # Prim's Algorithm in Python

INF = 9999999
# number of vertices in graph
N = 5
#creating graph by adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1