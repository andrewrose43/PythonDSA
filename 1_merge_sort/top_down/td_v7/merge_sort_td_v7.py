def merge_sort(arr: list):
    aux = [0]*len(arr)
    _merge_sort(arr, aux, 0, len(arr)-1)


# Note: hi is the length of the array, not the highest index, in this implementation
def _merge_sort(arr: list, aux: list, lo: int, hi: int):
    if lo < hi:
        #divide
        mid = lo+(hi-lo)//2
        #conquer
        _merge_sort(arr, aux, lo, mid)
        _merge_sort(arr, aux, mid+1, hi)
        #combine
        _merge(arr, aux, lo, mid, hi)


def _merge(arr: list, aux: list, curr: int, mid: int, hi: int):

    l_ind = curr
    r_ind = mid+1

    aux[curr:hi+1] = arr[curr:hi+1]

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
    # No need to copy the right side; it's already done.