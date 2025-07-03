"""
It appears there's an issue preventing the execution of the algorithm in this environment.
However, I can provide you with a detailed explanation of how you could implement Uniform-Cost Search (UCS)
in Python to solve the problem locally on your machine.
Uniform-Cost Search is a variant of Dijkstra's algorithm that is used for traversing a weighted tree or graph
to find the shortest path from a starting node to a goal node. It expands the least-cost node first and is guaranteed 
to find the least-cost path to the goal if the cost of each step exceeds some small positive value.
Here's a Python function for UCS using the PriorityQueue from the queue module:

"""
from queue import PriorityQueue
from typing import String ,List

def uniform_cost_search(graph, start, goal)-> List[int,str] : #->
    # Priority queue to hold the frontier nodes, initialized with the start node
    # Each element in the queue: (cost-so-far, current-node, path-so-far)
    frontier = PriorityQueue()
    # This inititalizes the starting.
    frontier.put((0, start, [start]))  #->  (0,Zerind, [Zerind])
    
    # A set to keep track of visited nodes
    explored = set()

    # Loop until the frontier is empty
    while not frontier.empty():  
        # Get the node in the frontier with the lowest cost-so-far
        cost, node, path = frontier.get_nowait()
        print(cost, node, path)

        # If the node is the goal, return the cost and path
        if node == goal:
            return cost, path

        # If the node has not been visited yet
        if node not in explored:
            explored.add(node)

            # Add neighbors to the frontier with updated costs and paths
            for neighbor, edge_cost in graph[node]:
                if neighbor not in explored:
                    frontier.put((cost + edge_cost, neighbor, path + [neighbor]))
 
    # If the goal was never reached in the search
    return float("inf"), []
"""
    You can use the following graph structure to represent the Romania map.
    The graph is a dictionary where each key is a city and each value is a
    list of tuples (neighbor, distance):   
    """
romania_map = {
    # Add the other cities and distances based on your image
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Craiova': [('Rimnicu Vilcea', 146), ('Pitesti', 138), ('Drobeta', 120)],
    'Drobeta': [('Craiova', 120), ('Mehadia', 75)],
    'Mehadia': [('Drobeta', 75), ('Lugoj', 70)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)]
}
"""To find the shortest path from Zerind to Bucharest using the UCS algorithm,
   you would call the function as follows:

   """

cost, path = uniform_cost_search(romania_map, 'Zerind', 'Bucharest')
print(f"Cost: {cost}, Path: {path}")

""" Run this script in your local Python environment after completing 
the romania_map with all the necessary connections based on the map provided.
The function will output the total travel distance and the sequence of cities
you would travel through to get from Zerind to Bucharest with the least cost using
 the Uniform-Cost Search algorithm. ​
 """