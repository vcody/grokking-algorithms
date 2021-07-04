from random import randint
'''
- Ch.1 Notes:
# Best case: log(n)
# Worst case: n

# Big O run times (Fastest => Slowest):
# 1. log(n)
# 2. n
# 3. n * log(n)
# 4. n ^ 2
# 5. n! 
'''

def generate_random_array(length):
    arr = []
    for i in range(0, length):
        # Add random int in range 0-100
        arr.append(randint(0, 100))
    
    return arr

def binary_search(array, item):
    # If array isn't sorted, sort it
    if (array != array.sort()): 
        array.sort()
    
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        # Check middle index
        midpoint = (start_index + end_index)
        guess = array[midpoint]

        if guess == item:
            print("Found at index", midpoint)
            return True
        # If guess too high...
        if guess > item:
            end_index = midpoint - 1
        # If guess too low...
        else:
            start_index = midpoint + 1
    return False

arr = generate_random_array(10)
random_item = arr[randint(0, len(arr))]

print("Array:", arr)
print("Number selected:", random_item)

print(binary_search(arr, random_item)) # True
print(binary_search(arr, 250)) # False

'''
- Exercises:
# 1.1: 7, since 2 ^ 7 = 128
# 1.2: 8, since 2 ^ 8 = 256

# Exercises 
# 1.3: log(n) - binary search 
# 1.4: n - linear time search
# 1.5: n - linear time search
# 1.6: n - linear time search
'''