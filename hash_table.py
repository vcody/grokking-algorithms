# AKA maps AKA dictionaries AKA associative arrays

inventory = {}
inventory['weapon'] = 'schimitar'
inventory['offhand'] = 'wand'
inventory['armor'] = 'light'

print(inventory)

store = {}
store['apple'] = 0.78
store['grapes'] = 3.25
store['bread'] = 2.50

print(store)

# Exercises
# 5.1. Yes
# 5.2. No
# 5.3. No
# 5.4. Yes

# Cache example (uses hashing)
cache = {}

def get_data_from_server(url):
    return "dummy function"

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

# Simple collision solution - linked list for multiple keys at slot
# This can create issues; pay attention to your hash function
# Hash tables:
#   - Fast as arrays at searching
#   - Fast as linked lists at insert/delete

# When considering collision avoidance...
# 1. Load factor: (# items in table / total # of slots)
#   - If load factor > .07, resizing is needed
#   - Generally, array is then doubled in size
# 2. Good hash function
#   - Distributes values evenly in array

# Exercises
# 5.5. C
# 5.6. B
# 5.7. D