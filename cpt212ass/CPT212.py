from pydoc import ispath
import random as rd
from os import system, name
from turtle import distance
import sys # Library for INT_MAX

# remove later just for troubleshooting purposes

# Class to represent graph and all the functions
class Graph:
    """ Constructor """

    def __init__(self, vertex):

        self.V = vertex
        self.exist = False
        self.edgeList = []  # List to store all edges in the graph
        self.Node = ["SE", "TO", "HA", "DU", "CA"]  # Store all vertices in a list
        self.adjList = {}  # Dictionary to represent adjacency list

        for node in self.Node:
            self.adjList[node] = {}  # Create dictionary for each vertex

        self.adjList['SE']['TO'] = 1156  # Default graph
        self.adjList['SE']['HA'] = 10915
        self.adjList['HA']['CA'] = 7624
        self.adjList['DU']['CA'] = 6072
        self.adjList['DU']['TO'] = 7933
       

    # Initial edge list
    def initial_edgelist(self, graph):
        for node in graph:
            for n in graph[node]:
                self.edgeList.append((node, n))
        return self.edgeList

    # Function to add edge
    def add_edge(self, src, destination, distance):

        self.adjList[src][destination] = distance
        self.adjList[destination][src] = distance

    # Function to add edge manually by user
    def add_edge_manual(self):

        self.exist = True
        src, dest = None, None

        self.printGraph()

        while self.exist:

            while True:

                print("Enter start and destination city from the list below:")
                print(list(self.adjList))
                src = input("Enter start city: ")
                dest = input("Enter destination city: ")

                if src.isalpha() and dest.isalpha():
                    if src == dest:
                        print("Unable to add an edge to the same city! Enter Again\n")
                    elif src not in self.adjList.keys():
                        print(src + " is not in the graph! Enter again!\n")
                    elif dest not in self.adjList.keys():
                        print(dest + " is not in the graph! Enter again!\n")
                    else:
                        break
                else:
                    print("Invalid Input! Try Again!\n")

            new_edge = (src, dest)

            # Check the existence of the new edge
            if new_edge in self.initial_edgelist(self.adjList):
                print()
                print("Edge", src, "to", dest, "already exist in the graph! Try again!")
                self.exist = True

            elif new_edge not in self.initial_edgelist(self.adjList):
                self.exist = False
                break

        weight = self.edge_weight(src, dest)

        self.add_edge(src, dest, weight)
        print("Edge", src, "to", dest, "with distance", weight, "is added into the graph!\n2")

    # Function to add random edge
    def add_newRandomEdge(self):

        self.exist = True  # Flag for existence of edges
        source, dest, weight = None, None, None
        # Check if edge exist in the graph
        while self.exist:

            citylist = ["SE", "TO", "HA", "DU", "CA"]  # List of all cities
            source = rd.choice(citylist)  # Random get one city as source city
            citylist.remove(source)  # Random get one city as destination from rest of the city
            dest = rd.choice(citylist)  # to prevent self loop

            new_edge = (source, dest)

            # Check the existence of the new edge
            if new_edge in self.initial_edgelist(self.adjList):
                self.exist = True

            elif new_edge not in self.initial_edgelist(self.adjList):
                break

        weight = self.edge_weight(source, dest)

        self.add_edge(source, dest, weight)  # Add to adjacency list
        # Print result
        print("Edge", source, "to", dest, "with distance", weight, "is added into the graph!\n")

    @staticmethod  # Determine the distance between cities
    def edge_weight(source, dest):

        weight = None

        if source == 'SE':
            if dest == 'TO':
                weight = 1156
            elif dest == 'HA':
                weight = 10915
            elif dest == 'DU':
                weight = 6780
            elif dest == 'CA':
                weight = 10814

        elif source == 'TO':
            if dest == 'SE':
                weight = 1156
            elif dest == 'HA':
                weight = 12126
            elif dest == 'DU':
                weight = 7933
            elif dest == 'CA':
                weight = 11597

        elif source == 'HA':
            if dest == 'SE':
                weight = 10915
            elif dest == 'TO':
                weight = 12126
            elif dest == 'DU':
                weight = 12961
            elif dest == 'CA':
                weight = 7252

        elif source == 'DU':
            if dest == 'SE':
                weight = 6780
            elif dest == 'TO':
                weight = 7933
            elif dest == 'HA':
                weight = 12961
            elif dest == 'CA':
                weight = 6072

        elif source == 'CA':
            if dest == 'SE':
                weight = 10814
            elif dest == 'TO':
                weight = 11597
            elif dest == 'HA':
                weight = 7252
            elif dest == 'DU':
                weight = 6072

        return weight

    # Function to reset default graph
    def reset_graph(self):
        print("Graph has been reset!")
        return self.__init__()

    # Function to remove an edge
    def remove_edge(self):

        self.printGraph()

        while True:
            # Ask user input
            print("Enter edge you want to remove")
            src = input("Please enter start city: ")
            dest = input("Please enter destination city: ")

            if src.isalpha() and dest.isalpha():
                if src not in self.adjList.keys():
                    print(src + " is not in the graph! Enter again!\n")
                elif dest not in self.adjList.keys():
                    print(dest + " is not in the graph! Enter again!\n")
                else:
                    try:
                        del self.adjList[src][dest]
                        print("Edge", src, "-", dest, "has been removed!\n")
                        break
                    except KeyError:
                        print("Edge is not found in the graph, Please try again!\n")
            else:
                print("Invalid Input! Try Again!\n")

    # Print adjacency list of graph
    def printGraph(self):
        edge = []
        for node in self.adjList.keys():
            print(node, "->", self.adjList[node])
        print()
        print(self.adjList["SE"].items())
        print(len(self.adjList))
    
    def is_path(t, path):
        if t.head != path[0]:
            return False
        if t.head == path[0] and len(path) == 1:
            return True
        return any(ispath(i, path[1:]) for i in t.children)
    
    def convert(self, V):
 
        # Initialize a matrix
        matrix = [[0 for j in range(V)]
                    for i in range(V)]
        
        for i in self.adjList:
            for j in self.adjList[i]:
                matrix[i][j] = 1
        
        return matrix

    """-----------------Function 1: Strongly connectivity--------------"""

    def DFSUSC(self, v, visited):
        # Mark the current node as visited and print it
        visited[self.Node.index(v)] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.adjList[v]:
            if not visited[self.Node.index(i)]:
                self.DFSUSC(i, visited)
   
    # Function that returns reverse (or transpose) of this graph
    def getTranspose(self):
        GRAPH = Graph()
        for i in self.adjList:
            GRAPH.adjList[i].clear()
        # Recur for all the vertices adjacent to this vertex
        for i in self.adjList:
            for j in self.adjList[i]:
                GRAPH.add_edge(j, i, self.adjList[i][j])
        return GRAPH

    # The main function that finds and prints all strongly
    # connected components
    def CheckStronglyConnected(self):
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * (len(self.Node))
        # Fill vertices in stack according to their finishing
        # times
        self.DFSUSC(self.Node[0], visited)

        # Create a reversed graph
        gr = self.getTranspose()
        visited = [False] * (len(self.Node))
        gr.DFSUSC(self.Node[0], visited)

        for n in range(0, 4):
            if not visited[n]:
                self.printGraph()
     
                return False

        return True

    def StronglyConnected(self):
        while not self.CheckStronglyConnected():
            print("Adding a new random edge \n")
            self.add_newRandomEdge()
        return True

    """-----------------Function 2: Cycle detection--------------"""
    
    def cycleDFS(self, node, visited, tracker, path):
        # mark current node as visited and add to tracker
        visited[self.Node.index(node)] = True
        tracker[self.Node.index(node)] = True
        # to store the path of cycle
        path.append(node)

        # if any neighbour is visited and in tracker then graph is cyclic
        for neighbour in self.adjList[node]:
            if not visited[self.Node.index(neighbour)]:
                if self.cycleDFS(neighbour, visited, tracker, path):
                    return True
            elif tracker[self.Node.index(neighbour)]:
                path.append(neighbour)
                return True

        # pop the node after the end of recursion
        tracker[self.Node.index(node)] = False
        return False

    def cycleDetection(self):
        visited = [False] * (len(self.Node))
        tracker = [False] * (len(self.Node))
        city_list = []
        for node in self.Node:
            if not visited[self.Node.index(node)]:
                if self.cycleDFS(node, visited, tracker, city_list):
                    print("Graph is cyclic!")
                    self.printCycle(city_list, visited, tracker)
                    print("-------------------------------")
                    return True

            city_list.clear()
            visited = [False] * (len(self.Node))
        return False

    def printCycle(self, path_track, visited, tracker):
        path = len(path_track)
        print()
        print("The cycle path is:")
        for city in path_track:
            path = path - 1
            if path == 0:
                print(city, end='')
                break
            if visited[self.Node.index(city)] & tracker[self.Node.index(city)]:
                print(city, end="->")
        print()

    def cycle(self):

        self.printGraph()
        print("Detecting cycle in the graph...")

        detected = self.cycleDetection()
        while detected == 0:
            print("Graph is not cyclic!")
            print()
            print("Adding random edge until a path exists...")
            self.add_newRandomEdge()
            detected = self.cycleDetection()

            if detected == 1:
                break

    """-----------------Function 3: Shortest path between two vertex--------------"""

    # Dijkstra algorithm to find shortest path
    def dijkstra(self, src, end):

        prev = {}  # List to store precedent vertex
        shortestDistance = {}  # Record the weight
        graphlist = self.adjList.copy()
        path = []  # Find optimal node

        for node in graphlist:
            shortestDistance[node] = float('inf')
        shortestDistance[src] = 0

        # Compare the distance between different path
        while graphlist:
            min_dis = None
            for node in graphlist:
                if min_dis is None:
                    min_dis = node
                elif shortestDistance[node] < shortestDistance[min_dis]:
                    min_dis = node
                    
            path_option = self.adjList[min_dis].items()

            for data, dis in path_option:

                if dis + shortestDistance[min_dis] < shortestDistance[data]:
                    shortestDistance[data] = dis + shortestDistance[min_dis]
                    prev[data] = min_dis

            graphlist.pop(min_dis)

        currentNode = end

        # Add city to the path list
        while currentNode != src:
            try:
                path.insert(0, currentNode)
                currentNode = prev[currentNode]

            except KeyError:
                break

        path.insert(0, src)

        # Print the result when a path is found
        if shortestDistance[end] != float('inf'):
            print("Shortest distance is: " + str(shortestDistance[end]))
            print("The shortest path is: ", end='')
            for city in path:
                if city in path[-1]:
                    print(city, end='')
                else:
                    print(city, end='->')
            print("\n---------------------------------")
        else:
            prev = None

        return prev
        

    # Function to run the find path function
    def shortestPath(self):

        self.printGraph()

        while True:

            print("Enter start and destination city from the list below:")
            print(list(self.adjList))
            src = input("Please enter start city: ")
            dest = input("Please enter destination city: ")

            if src not in self.adjList.keys():
                print(src + " is not in the graph! Enter again!\n")
            elif dest not in self.adjList.keys():
                print(dest + " is not in the graph! Enter again!\n")
            else:
                break

        print("\nFinding shortest path from", src, "to", dest, "...")
        prev = self.dijkstra(src, dest)

        if prev is None:
            print("There is no path between", src, "and", dest)
            print()
            getinput = input("Do you want to add random edge until a path exists?(y for yes/ Any key to exit): ")

            if getinput == 'y':
                while prev is None:
                    self.add_newRandomEdge()
                    print("Finding shortest path from", src, "to", dest, "...\n")
                    prev = self.dijkstra(src, dest)

    """-----------------Function 4: Finding Minimum Spanning Tree--------------"""
<<<<<<< HEAD
    
    """ def PrimMST(self):
        # Get the number of vertices in graph
        V = self.V
 
        # key values used to pick minimum weight edge in cut
        key = []
 
        # List to store constructed MST
        parent = []
 
        # minHeap represents set E
        minHeap = Heap()
 
        # Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for v in range(V):
            parent.append(-1)
            key.append(1e7)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)
 
        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])
 
        # Initially size of min heap is equal to V
        minHeap.size = V
 
        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:
 
            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
 
            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[u]:
 
                v = pCrawl[0]
 
                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
 
                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])
 
        printArr(parent, V)  """

=======
    #Function to find path
    def PrimMST(self):

        key = []
        weight = []
        len = 0
        src = "SE"
        
        path_option = self.adjList[src].items()
        key.append(src)

        for node, distance in path_option:
            data1 = 1157
            if distance < data1:
                key.append(node)
                weight.append(distance)

        next = key[1]
        self.add_edge(next, 'DU', 7933)
        self.add_edge(next, 'HA', 12126)
        for node, distance in self.adjList[next].items():
            data1 = 12126
            if distance < data1:
                key.append(node)
                weight.append(distance)

        next = key[2]
        for node, distance in self.adjList[next].items():
            data1 = 7933
            if distance < data1:
                key.append(node)
                weight.append(distance)

        next = key[3]
        self.add_edge(next, 'SE', 10814)
        self.add_edge(next, 'HA', 7252)
        for node, distance in self.adjList[next].items():
            data1 = 10814
            if distance < data1:
                key.append(node)
                weight.append(distance)

        print("Minimum Spanning Tree: \n")
        for x in key:
            print(x)
        for x in weight:
            len += x
        print("Total length is ", len)



>>>>>>> f59b6b17430f1b3308b6c757a6aec90bd18fa9f0
# Function to clear screen
def cls_screen():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


# Function to validate user input
def userInput():
    while True:
        try:
            option = int(input("Select option to perform: "))
            if 0 > option > 5:
                print("Invalid input, Please try again.")
            else:
                return option
        except ValueError:
            print("Invalid input, Please try again.")


def print_menu():
    # Print menu
    print("=========================================================")
    print("=  1. Graph Connectivity                                =")
    print("=  2. Cycle Detection                                   =")
    print("=  3. Shortest Path                                     =")
    print("=  4. Minimum Spanning Tree                             =")
    print("=  5. Reset The Graph to Default                        =")
    print("=  6. Add an Edge                                       =")
    print("=  7. Remove an Edge                                    =")
    print("=  8. View Graph Adjacency List                         =")
    print("=  9. Exit/Quit                                        =")
    print("=========================================================")


def city_name():
    # Label all cities short form
    print("* SE : Seoul, South Korea   *")
    print("* TO : Tokyo, Japan         *")
    print("* HA : Havana, Cuba         *")
    print("* DU : Dubai, UAE           *")
    print("* CA : Casablanca, Morocco  *")


def AWAIT_TRIGGER():

    input("PRESS ANYTHING TO CONTINUE")


def main():

    g = Graph(5)  # Create a graph
    print()
    city_name()
    print()
    print("Adjacency List of the graph:")
    g.printGraph()


    while True:

        print_menu()  # Print menu
        choice = userInput()  # Get user input
        cls_screen()

        while choice:
            if choice == 1:
                if g.StronglyConnected():
                    g.printGraph()
                   
                    AWAIT_TRIGGER()
                    cls_screen()
                break
            elif choice == 2:
                g.cycle()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 3:
                g.shortestPath()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 4:
               # g.PrimMST()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 5:
                g.reset_graph()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 6:
                g.add_edge_manual()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 7:
                g.remove_edge()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 8:
                city_name()
                print()
                print("Adjacency List of the graph:")
                g.printGraph()
                AWAIT_TRIGGER()
                cls_screen()
                break
            elif choice == 9:
                print("EXITING PROCESSES....\n")
                exit()


if __name__ == "__main__":
    main()
