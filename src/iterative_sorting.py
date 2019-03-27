def swap_arr_elements(arr, index_a, index_b):
    temp = arr[index_a]
    arr[index_a] = arr[index_b]
    arr[index_b] = temp

    return arr

# TO-DO: Complete the selection_sort() function below


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr = swap_arr_elements(arr, smallest_index, cur_index)

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_occured = True
    while swap_occured:
        swap_occured = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr = swap_arr_elements(arr, i, i+1)
                swap_occured = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
