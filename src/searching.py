# STRETCH: implement Linear Search
def linear_search(arr, target):

    # TO-DO: add missing code

    return -1   # not found

# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty
    left = 0
    right = len(arr) - 1

    # TO-DO: add missing code
    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            right = middle - 1
        elif target > arr[middle]:
            left = middle + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)/2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
