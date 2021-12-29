'''
first_occurence
'''

arr = [2, 4, 10, 10, 10, 18, 20, 20, 27]
print(arr)

def binarysearch(arr, start, end, k):
    if start > end:
        return -1
    if start == end:
        if arr[start] == k:
            return start
        else:
            return -1
    mid = int((start + end) / 2)
    if arr[mid] == k:
       return binarysearch(arr, start, mid, k)
    elif arr[mid] > k :
        return binarysearch(arr, start, mid-1, k)
    else:
        return binarysearch(arr, mid+1, end, k)


print(binarysearch(arr, 0, len(arr)-1, 20))