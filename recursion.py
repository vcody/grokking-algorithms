'''
- Ch. 3 Notes:
- Recursion defined as a process with:
    1. Base case
    2. Recursive case
- Stack (LIFO)
- Recursion, in a sense, exploits stack to loop through said object
- Though useful, it requires stack memory allocation that is dynamic, and can be costly
    - Solved via loops / "tail recursion"
'''

# Basic recursive function
def factorialize(begin_number):
    if begin_number <= 1:
        return 1
    else:
        return begin_number * factorialize(begin_number - 1)

for i in range(100):
    print("#" + str(i) + ". " + str(factorialize(i)))
