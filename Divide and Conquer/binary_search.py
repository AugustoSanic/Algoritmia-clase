
'''
Binary search implementation.
'''

def binary_search(arr, key, left=0, right=None):

    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, left, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, right)
