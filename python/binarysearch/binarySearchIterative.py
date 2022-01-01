arr = [1, 3, 5, 6, 9, 11, 33]


def binarySearchIterative(arr, k):
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = start + (end - start) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    return -1

print(binarySearchIterative(arr, 33))