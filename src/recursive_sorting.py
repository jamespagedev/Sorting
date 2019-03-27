# TO-DO: complete the helper function below to merge 2 sorted arrays

# from lambda video (not working) - https://www.youtube.com/watch?v=RaNLB4XOOIs
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements
#     # TO-DO
#     for i in range(len(merged_arr)):
#         if not arrA:
#             merged_arr.append(arrB)
#         elif not arrB:
#             merged_arr.append(arrA)
#         elif arrA[0] < arrB[0]:
#             merged_arr[i] = arrA[0]
#         else:
#             merged_arr[i] = arrB[0]

#     return merged_arr


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # edge case
    if len(arr) < 2:
        return arr

    # TO-DO
    # divide
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    # conquer
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

# STRETCH: quick_sort is another popular sort that I didn't see in this repo... so I'm adding it


def quick_sort(arr):

    return arr
