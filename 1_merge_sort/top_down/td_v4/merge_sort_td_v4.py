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
    aux[lo:hi+1] = arr[lo:hi+1] # Pleased with this syntactic improvement here!

    # Zipper-merge
    left_ind = lo
    right_ind = mid+1
    for k in range(lo, hi+1):
        if left_ind > mid:
            arr[k] = aux[right_ind]
            right_ind += 1
        elif right_ind > hi:
            arr[k] = aux[left_ind]
            left_ind += 1
        elif aux[left_ind] < aux[right_ind]:
            arr[k] = aux[left_ind]
            left_ind += 1
        else:
            arr[k] = aux[right_ind]
            right_ind += 1