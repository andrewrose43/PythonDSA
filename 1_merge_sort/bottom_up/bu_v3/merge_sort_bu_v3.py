def merge_sort(arr: list):

    sz = 1
    while sz < len(arr):
        lo = 0
        replacement = [] # This will replace arr. Appending to replacement and then replacing arr with replacement is faster than inserting into arr.
        while lo < len(arr)-sz:
            replacement.extend(_merge(lo, arr[lo:lo+sz], arr[lo+sz:lo+2*sz]))
            lo += 2*sz
        replacement.extend(arr[lo:]) # New line! This captures any tail end of the array that wasn't already taken care of
        sz *= 2
        arr = replacement
    return arr


def _merge(curr: int, left: list, right: list):

    l_ind = r_ind = 0
    tmp = []
    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] < right[r_ind]:
            tmp.append(left[l_ind])
            l_ind += 1
        else:
            tmp.append(right[r_ind])
            r_ind += 1
        curr += 1

    if l_ind < len(left):
        tmp.extend(left[l_ind:])
    elif r_ind < len(right):
        tmp.extend(right[r_ind:])

    return tmp
