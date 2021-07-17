'''
Dijkstra's Algorithm steps:
    1. Find "cheapest" node
    2. Check if neighbors are cheaper. If yes, update
    3. Repeat for every node
    4. Calculate final path
- Works with "directed acylic graphs"
- Does not work with negative-weight edges
    -> Use Bellman-Ford algorithm (todo)
'''

# ch7_example.png:

graph = {}

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed= []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# While we have nodes to process...
# 1. Grab node closest to start
# 2. Update costs for its neighbors
# 3. If any neighbors costs were updated, update parents also
# 4. Mark node as processed, repeat until finished

# Find cheapest node
node = find_lowest_cost_node(costs)
# Look through all nodes not processed yet
while node is not None:
    print("Node:", node)

    cost = costs[node]
    neighbors = graph[node]

    print("cost/neighbors:", cost, neighbors)
    
    # Check all neighbors
    for n in neighbors.keys():
        print("n:", n) 

        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            # Update cost
            costs[n] = new_cost
            # Node becomes new parent for neighbor
            parents[n] = node
    processed.append(node)
    # Find next node, repeat
    node = find_lowest_cost_node(costs)
