def quicksort(lst: list):
    _quicksort(lst, 0, len(lst)-1)

def _quicksort(lst: list, lo: int, hi: int):
    if lo < hi:
        p = _partition(lst, lo, hi)
        _quicksort(lst, lo, p-1)
        _quicksort(lst, p+1, hi)

def _partition(lst: list, lo: int, hi: int):
    i = lo
    pivot = lst[hi]  # Cached for speed
    while lo < hi:  # Leave pivot untouched
        if lst[lo] < pivot:
            lst[lo], lst[i] = lst[i], lst[lo]
            i += 1
        lo += 1
    lst[i], lst[hi] = pivot, lst[i]
    return i