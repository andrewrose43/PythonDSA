def merge_sort(arr: list):
    aux = [0]*len(arr) # auxiliary array
    _merge_sort(arr, aux, 0, len(arr) - 1)


def _merge_sort(arr: list, aux: list, lo: int, hi: int):

    if lo >= hi:
        return
    # divide: get mid
    mid = int(lo + (hi-lo)/2) # Note: for succinctness, use // next time instead of casting
    # conquer: call _sort on the halves
    _merge_sort(arr, aux, lo, mid)
    _merge_sort(arr, aux, mid + 1, hi)
    # combine: call merge between lo and hi
    _merge(arr, aux, lo, mid, hi)


def _merge(arr: list, aux: list, lo: int, mid: int, hi: int):
    for k in range(lo, hi+1): # +1 to include the hi index
        aux[k] = arr[k] # create backup

    # Prep for zipper merge
    i = lo
    j = mid + 1

    # Zipper merge
    for k in range(lo, hi+1): # +1 to include the hi index
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1
