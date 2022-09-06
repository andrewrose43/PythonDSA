def merge_sort(arr: list):

    sz = 1
    while sz < len(arr):
        lo = 0
        while lo < len(arr)-sz:
            _merge(arr, lo, arr[lo:lo+sz], arr[lo+sz:lo+2*sz])
            lo += 2*sz
        sz *= 2


def _merge(arr: list, lo: int, left: list, right: list):

    curr = lo
    l_ind = r_ind = 0
    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] < right[r_ind]:
            arr[curr] = (left[l_ind])
            l_ind += 1
        else:
            arr[curr] = (right[r_ind])
            r_ind += 1
        curr += 1

    if l_ind < len(left):
        arr[curr:curr+(len(left)-l_ind)] = left[l_ind:]
    elif r_ind < len(right):
        arr[curr:curr+(len(right)-r_ind)] = right[r_ind:]