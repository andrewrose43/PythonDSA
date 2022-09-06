def merge_sort(arr: list):
    aux = [0]*len(arr) # Need this to merge in place
    _merge_sort(arr, aux, 0, len(arr) - 1)


def _merge_sort(arr: list, aux: list, lo: int, hi: int):
    if lo < hi: # Only do anything if there are 2+ items to work with
        # Divide
        mid = lo + (hi-lo)//2
        # Conquer
        _merge_sort(arr, aux, lo, mid)
        _merge_sort(arr, aux, mid + 1, hi)
        # Combine
        _merge(arr, aux, lo, mid, hi)


def _merge(arr: list, aux: list, lo: int, mid: int, hi: int):

    # Copy contents being merged into aux
    aux[lo:hi+1] = arr[lo:hi+1]

    l_ind = lo
    r_ind = mid+1
    curr = lo
    while l_ind <= mid and r_ind <= hi:
        if aux[l_ind] < aux[r_ind]:
            arr[curr] = aux[l_ind]
            l_ind += 1
        else:
            arr[curr] = aux[r_ind]
            r_ind += 1
        curr += 1

    for k in range(l_ind, mid + 1):
        arr[curr] = aux[k]
        curr += 1
    for k in range(r_ind, hi + 1):
        arr[curr] = aux[k]
        curr += 1