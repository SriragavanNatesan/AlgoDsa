arr = [1, 3, 5, 6, 9, 11, 33]

def binarysearch(arr, start, end, k):
    if start >= end:
        return -1
    mid  = int((start + end) / 2)
    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        return binarysearch(arr, start, mid-1, k)
    else:
        return binarysearch(arr, mid+1, end, k)

print(binarysearch(arr, 0, len(arr), 4))