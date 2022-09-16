def quicksort(lst: list):
    _quicksort(lst, 0, len(lst)-1)


def _quicksort(lst: list, lo: int, hi: int):
    if lo < hi:
        p = _partition(lst, lo, hi)
        _quicksort(lst, lo, p-1)
        _quicksort(lst, p+1, hi)


def _partition(lst: list, lo: int, hi: int):
    i = lo
    pivot_item = lst[hi]  # The partition, cached to avoid lots of individual access operations later
    while lo < hi:  # Notice that the last item of the list is excluded; it's saved for use as the partition
        if lst[lo] < pivot_item:
            # Get all the less-than-pivot values shuffled to the left
            tmp = lst[i]
            lst[i] = lst[lo]
            lst[lo] = tmp
            i += 1
        lo += 1
    # Now get the pivot between the two halves
    lst[hi] = lst[i]
    lst[i] = pivot_item
    # Return the pivot's index
    return i
