#1. Breadth First Search
def BFS(G, s):
    
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

#2. Depth First Search

#3. Depth First Search for Tree/Forest

#4. Topological Sorting

#5. Krushkal's Algorthm

#6. Prim/Dijkstra MST algorithm


def main():
    V = ('a','b','c','d','e','f','g')
    E = [('a', 'b'), ('a','d'), ('a','e'), ('b','d'), ('b','e'), ('d','e'), ('a','c'), ('c','f'), ('c','g'),('f','g')]
    G = [V, E]
    BFS(G, 0)


main()