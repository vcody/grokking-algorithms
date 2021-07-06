from random import randint

'''
- Ch. 2 Notes:
- Linked lists have slow reads, fast inserts
    - Reads faster/slower depending on # iterations
- Arrays have fast reads, slow inserts
- Linked lists faster for middle inserts, and deletions
'''

def generate_random_array(length):
    arr = []
    for i in range(0, length):
        # Add random int in range 0-100
        arr.append(randint(0, 100))
    
    return arr

def find_smallest(array):
    # Start w/ first element
    min_item = array[0]
    min_index = 0

    for i in range(1, len(array)):
        if array[i] < min_item:
            min_item = array[i]
            min_index = i
    # print("Smallest element in array is", min_index)
    return min_index

def selection_sort(array):
    sorted_array = [] 
    for i in range(len(array)):
        min_item = find_smallest(array)
        sorted_array.append(array.pop(min_item))
    return sorted_array

random_arr = generate_random_array(10)
print("Pre-sort:", random_arr)
print("Post-sort:", selection_sort(random_arr))

'''
- Exercises:
2.1: Linked list, since there aren't many iterations through data needed
2.2: Linked list, since there aren't reads needed except the last item
2.3: Array, as a linked list would require iteration to reach half-way
2.4: Arrays have to reallocate items in memory around that insert
2.5: Searching -- arrays: slower, linked lists: faster
    cont.) Inserting -- arrays: faster, linked lists: no difference
'''