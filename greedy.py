# Greedy: at each step, pick optimal move
# Pick each locally optimal move, end up with globally optimal solution

# Exercises
# 8.1. Fill largest -> smallest boxes. 
# 8.2. Pick the highest point total that is the shortest distance

# Approximation algorithm, judged by:
# 1. How fast they are
# 2. How close they are to optimal solution

# Ex.) 
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['k1'] = set(['id', 'nv', 'ut'])
stations['k2'] = set(['wa', 'id', 'mt'])
stations['k3'] = set(['or', 'nv', 'ca'])
stations['k4'] = set(['nv', 'ut'])
stations['k5'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        # & = set intersection
        # - = set difference
        # | = set union
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)

# Exercises
# 8.3. No
# 8.4. Yes
# 8.5. Yes

# NP-complete (Set-covering): 
# Calculate every possible solution, then pick smallest one
# Signs:
# 1. Runs quickly with small amount of items, gets much slower with more
# 2. "All combinations of _" ...
# 3. Calculating every possible version of _; can't break down problem
# 4. Involves a sequence (e.g. sequence of cities) and is hard to solve
# 5. Involves set (e.g. set of radio stations) and is hard to solve
# 6. Can you restate it as a set-covering or traveling-salesperson problem?

# Exercises
# 8.6. Yes
# 8.7. Yes
# 8.8. Yes