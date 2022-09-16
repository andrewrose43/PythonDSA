def quicksort(lst: list):
    return _quicksort(lst, 0, len(lst)-1)

def _quicksort(lst: list, lo: int, hi: int):
    if lo < hi:
        p = _partition(lst, lo, hi)
        _quicksort(lst, lo, p-1)
        _quicksort(lst, p+1, hi)

def _partition(lst: list, lo: int, hi: int):
    i = lo
    pivot = lst[hi]  # cached for speed
    for j in range(lo, hi):  # note how this excludes the final item
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[hi] = pivot, lst[i]
    return i