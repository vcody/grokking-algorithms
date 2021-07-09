from collections import deque

# Breadth-first search effective for shortest path problems
# Graph as "set of connections" with nodes/edges
# Queue: FIFO / Stack: LIFO

# Exercises
# 6.1. 2
# 6.2. 2

# ex.)
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue = deque()
search_queue += graph['you']

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, "is a mango seller.")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search('you'))

# Running time for network AT LEAST O(# edges)
# Running time for queue AT LEAST O(n) for n=# people
# So... BFS takes -> O(# people + # edges) or O(V+E)

# Exercises
# 6.3. No / Yes / No
# 6.4. Wake up -> Brush Teeth -> Pack Lunch -> Eat Breakfast -> Exercise ...

# Tree as graph with no edges that point back

# Exercises
# 6.5. A/C
