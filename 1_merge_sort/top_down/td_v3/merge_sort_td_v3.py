def merge_sort(arr: list):
    _merge_sort(arr, 0, len(arr) - 1)


def _merge_sort(arr: list, lo: int, hi: int):
    if lo < hi: # Only do anything if this sublist is at least 2 elements long
        # divide
        mid = lo + (hi-lo)//2
        # conquer
        _merge_sort(arr, lo, mid)
        _merge_sort(arr, mid + 1, hi)
        # combine
        _merge(arr, lo, mid, hi)


def _merge(arr: list, lo: int, mid: int, hi: int):

    # Temporary lists to hold contents to be zipper-merged
    left = [0]*(mid-lo+1)
    right = [0]*(hi-mid)

    # Now fill the temporary lists
    left_ind = right_ind = 0
    for k in arr[lo:mid+1]:
        left[left_ind] = k
        left_ind += 1
    for k in arr[mid+1:hi+1]:
        right[right_ind] = k
        right_ind += 1

    # Zipper merge
    left_ind = right_ind = 0
    for k in range(lo, hi+1):
        if left_ind >= len(left):
            arr[k] = right[right_ind]
            right_ind += 1
        elif right_ind >= len(right):
            arr[k] = left[left_ind]
            left_ind += 1
        elif left[left_ind] < right[right_ind]:
            arr[k] = left[left_ind]
            left_ind += 1
        else:
            arr[k] = right[right_ind]
            right_ind += 1