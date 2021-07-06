from random import randint
'''
- Ch. 4 Notes
- Divide & Conquer algorithms (ex. quicksort)
    1. Figure out base (simplest possible) case
    2. Divide/decrease problem until it becomes base case
- Quicksort has smaller O(n log n) constant time than merge sort
'''

def generate_random_array(length):
    arr = []
    for i in range(length):
        arr.append(randint(0, 500))
    # Better way to do this below?
    return list(set(arr))

# Exercise 4.1
def recursive_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array.pop() + recursive_sum(array)

l = [2,4,6]
print("Sum comparisons:")
print(sum(l)) # 12
print(recursive_sum(l)) # 12

# Reset l
l = [2,4,6]

# Exercise 4.2
def recursive_count_items(array):
    if array == []: return 0
    else:
        array.pop()
        return 1 + recursive_count_items(array)

print("Count comparisons:")
print(len(l)) # 3
print(recursive_count_items(l)) # 3

# Reset l
l = [2,4,6]

# Exercise 4.3
def recursive_find_max(array, max=0):
    if array == []: return max
    if array[0] > max:
        max = array.pop(0)
    return recursive_find_max(array, max)

print("Max comparisons:")
print(max(l)) # 6
print(recursive_find_max(l)) # 6

# Reset l
l = [6,2,4]
l2 = generate_random_array(5)

# Quicksort
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        numbers_less = [ i for i in array[1:] if i <= pivot ]
        numbers_more = [ i for i in array[1:] if i > pivot ]

        return quicksort(numbers_less) + [ pivot ] + quicksort(numbers_more)

print("Quicksort:")
print(quicksort(l)) # 2,4,6
print(quicksort(l2)) # Random array, answers vary

