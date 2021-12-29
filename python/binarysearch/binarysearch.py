arr = [1, 3, 5, 6, 9, 11, 33]

def binarysearch(arr, start, end, k):
    # print("start = {}, end={}".format(start, end))
    if start > end:
        return -1
    '''
    TO avoid mid overflow if len(arr) > 10^9
    mid = start +  int((end -start) / 2)    
    '''
    mid  = int((start + end) / 2)
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binarysearch(arr, start, mid-1, k)
    else:
        return binarysearch(arr, mid+1, end, k)

print(binarysearch(arr, 0, len(arr)-1, 33))