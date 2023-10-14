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
        neighbors[] = current.getNeighbors()
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