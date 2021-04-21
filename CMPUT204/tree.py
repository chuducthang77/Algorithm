#1. Breadth First Search
#1.1 BFS 1st implementation used mark array
def BFS_v1(G, s):
    
    vertex = G[0]
    edges = G[1]

    #Initialize the queue
    queue = []

    #Create a mark list to determine whether the vertex has been visited before
    mark = [False for i in range(len(vertex))]
    
    #Start with vertex at index s and append the queue
    start = vertex[s]
    queue.append(start)
    mark[s] = True

    #Pop the first item of the queue and append the neighbor of item to the queue
    while len(queue) != 0:
        current = queue.pop(0)
        print(current)
        neighbors = [neighbor[1] for neighbor in edges if neighbor[0] == current]
        for neighbor in neighbors:
            #Check if the neigbor has been marked
            index = vertex.index(neighbor)
            if mark[index] == False:
                mark[index] = True
                queue.append(neighbor)

#1.2 BFS second implementation used color
class Node:
    def __init__(self):
        self.name = None
        self.color = None
        self.parent = None
        self.distance = None
        self.neighbor = []
    
    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

    def get_parent(self):
        return self.parent
    
    def get_distance(self):
        return self.distance
    
    def get_neighbor(self):
        return self.neighbor

    def set_name(self, name):
        self.name = name
    
    def set_color(self, color):
        self.color = color

    def set_parent(self, parent):
        self.parent = parent
    
    def set_distance(self,distance):
        self.distance = distance

    def __str__(self):
        print(self.name)
        print(self.color)
        print(self.parent)
        #print(self.neighbor)
        print(self.distance)
    
def BFS_v2(G, s):
    vertex = G[0]
    edges = G[1]

    # Initialize the empty queue
    queue = []
    class_vertex =  []
    
    for vertice in vertex:
        item = Node()
        item.set_name(vertice)
        item.set_color('w')
        #Set the distance to be a big number
        item.set_distance(99999999)
        class_vertex.append(item)

    #Set the neighbor nodes
    for vertice in class_vertex:
        for edge in edges:
            if vertice.get_name() == edge[0]:
                index = vertex.index(edge[1])
                vertice.get_neighbor().append(class_vertex[index])

    #Choose the node at given index and add to queue
    item = class_vertex[s]
    item.set_distance = 0
    item.set_color = 'g'
    queue.append(item)

    while len(queue) != 0:
        choose = queue.pop(0)
        print(choose.get_name())
        neighbors = choose.get_neighbor()
        for neighbor in neighbors:
            if neighbor.get_color() == 'w':
                neighbor.set_distance(choose.get_distance() + 1)
                neighbor.set_parent(choose)
                neighbor.set_color('g')
                queue.append(neighbor)
        

#2. Depth First Search

#3. Depth First Search for Tree/Forest

#4. Topological Sorting

#5. Krushkal's Algorthm

#6. Prim/Dijkstra MST algorithm

def main():
    V = ('a','b','c','d','e','f','g')
    E = [('a', 'b'), ('a','d'), ('a','e'), ('b','d'), ('b','e'), ('d','e'), ('a','c'), ('c','f'), ('c','g'),('f','g')]
    G = [V, E]

    #First implementation used BFS v1
    # BFS_v1(G, 0)

    #Second implementation used class nodes
    BFS_v2(G,0)

main()