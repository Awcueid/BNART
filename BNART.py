class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def shortest_distance(self, start, end):
        queue = deque([(start, 0)])  # (node, distance)
        visited = set()

        while queue:
            node, distance = queue.popleft()
            if node == end:
                return distance

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    queue.append((neighbor, distance + 1))

        # If there is no path from start to end
        return -1

# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

start_node = 1
end_node = 6
distance = g.shortest_distance(start_node, end_node)
print(f"Shortest distance from node {start_node} to node {end_node} is {distance} units.")

# 0 - roads, 1 - buildings , 2 - intersections
GRID = [[[1],[0,12],[1]],
        [[0,7],[0,5],[1]],
        [[2,8.5],[0,7],[0,2]],
        [[1],[0,13],[2,7.5]]
        ]

Test_case = [[0,0],[3,0]] 

#Arc consistency

# def revise(csp, X, Y):
#     revised = False
#     for x in X.domain:
#         if(no y in Y.domain satisfies constraint for (X, Y)):
#             X.delete(x)
#             revised = True
#     return revised

# def AC(csp):
#     queue = new Queue()
#     # queue = all arcs in csp
#     for arc in csp:
#         queue.enqueue(arc)
    
#     while(queue):
#         (X, Y) = DEQUEUE(queue)
#         if revise(csp, X, Y):
#             if(size(X.domain) == 0):
#                 return flase
#         for each Z in X.neighbors - {Y}:
#             ENQUEUE(queue, (Z, X))
#     return true


def HILL_CLIMB(Sv, v, Dv):
    current = Sv
    
    while(current != Dv):
        # Get all neighbors
        neighbors = current.getNeighbors()
        # Distance to get to destination from current location
        best_distance = current.getDistance()
        # Compare distance to all other neighbors
        for curr_neighbor in neighbors:
            if curr_neighbor.getDistance() < best_distance:
                # Neighbor is better, update best neighbor and current
                current = curr_neighbor
                best_distance = curr_neighbor.getDistance()
                
    # End reached, return current
    return current



# Get distance will use BFS
def getDistance(G, start, end):
        queue = deque([(start, 0)])  # (node, distance)
        visited = set()

        while queue:
            node, distance = queue.popleft()
            if node == end:
                return distance

            if node not in visited:
                visited.add(node)
                for neighbor in G.graph[node]:
                    queue.append((neighbor, distance + 1))

        # If there is no path from start to 