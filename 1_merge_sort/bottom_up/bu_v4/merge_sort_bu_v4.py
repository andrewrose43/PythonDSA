def merge_sort(arr: list):
    sz = 1
    while sz < len(arr):
        aux = arr.copy()
        lo = 0
        while lo < len(arr) - sz:
            _merge(arr, aux, lo, lo+sz-1, min(len(arr)-1, lo+2*sz-1))
            lo += 2*sz
        sz *= 2

def _merge(arr: list, aux: list, curr: int, mid: int, hi: int):

    l_ind = curr
    r_ind = mid+1

    while l_ind <= mid and r_ind <= hi:
        if aux[l_ind] < aux[r_ind]:
            arr[curr] = aux[l_ind]
            l_ind += 1
        else:
            arr[curr] = aux[r_ind]
            r_ind += 1
        curr += 1

    if l_ind <= mid:
        arr[curr:hi+1] = aux[l_ind:mid+1]
    # No need to copy the right side, because, logically, it is already in the correct order if it hasn't been copied yet
