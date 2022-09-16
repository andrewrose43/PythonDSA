def quicksort(lst: list):
    _quicksort(lst, 0, len(lst)-1)

def _quicksort(lst: list, lo: int, hi: int):
    if lo < hi:
        p = _partition(lst, lo, hi)
        _quicksort(lst, lo, p-1)
        _quicksort(lst, p+1, hi)

def _partition(lst: list, lo: int, hi: int):
    pivot = lst[hi]
    i = lo
    for j in range(lo, hi):
        if lst[j] < pivot:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            i += 1
    lst[hi] = lst[i]
    lst[i] = pivot
    return i