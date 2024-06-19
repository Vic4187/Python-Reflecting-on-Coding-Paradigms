# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
