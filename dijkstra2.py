# Exercises, refer to: ch7_exercises.png
# a.) with nodes: start, fin, A, B, C, D
graph2 = {}

graph2['start'] = {}
graph2['start']['a'] = 5
graph2['start']['b'] = 2

graph2['a'] = {} 
graph2['a']['c'] = 4
graph2['a']['d'] = 2

graph2['b'] = {}
graph2['b']['a'] = 8
graph2['b']['d'] = 7

graph2['c'] = {}
graph2['c']['d'] = 6
graph2['c']['fin'] = 3

graph2['d'] = {}
graph2['d']['fin'] = 1

graph2['fin'] = {}

infinity = float('inf')

costs = {}
costs['a'] = 5 
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Find cheapest node
node = find_lowest_cost_node(costs)
print('Lowest:', node)

counter = 0

while node is not None:
    print(node)

    cost = costs[node]
    neighbors = graph2[node]

    print(cost, neighbors)

    for n in neighbors.keys():
        print(n)
        break

    break 