import heapq

# Define the graph as a dictionary where each node points to a dictionary of neighbors with distances
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Heuristic straight-line distance to Bucharest for each city
heuristics = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151,
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199,
    'Zerind': 374
}

def astar_search(graph, heuristics, start_state,destination):
    # The queue stores priority, node, cost to reach, and path taken
    #queue = [(heuristics[start_state], start_state, 0, [start_state])]
    queue = [(heuristics[start_state], start_state, 0, [start_state])]
    visited = set()

    while queue:
        # Pop the item with the lowest heuristic + cost
        _, current, cost, path = heapq.heappop(queue)
        print(_,current, cost, path)
        
        # If this node has been visited, skip it
        if current in visited:
            continue

        # If we're at the destination, return the cost and path
        if current == destination:
            return cost, path

        # Add the node to the set of visited nodes
        visited.add(current)

        # Add all neighbors to the queue with their respective priorities
        for neighbor, distance in graph[current].items():
            if neighbor not in visited:
                # Priority is the current cost plus the heuristic of the neighbor
                priority = cost + distance + heuristics[neighbor]
                heapq.heappush(queue, (priority, neighbor, cost + distance, path + [neighbor]))

    return float("inf"), []

# Using A* to find the shortest path from Timisoara to Bucharest
astar_search(romania_map, heuristics, 'Timisoara', 'Bucharest')
