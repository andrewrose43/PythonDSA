
def merge_sort(arr: list):

    aux = [0]*len(arr) # Temporary array

    x = 1 # size of sublists being merged
    while x < len(arr):
        y = 0 # index of the first of the two sublists being merged
        while y < len(arr): # Minor improvement to make in v2: make this y < len(arr)-x to avoid redundant work
            _merge(arr, aux, y, y+x-1, min(y+x+x-1, len(arr)-1))
            y += 2*x # move to next pair of sublists
        x *=2 # double size of next zipper merge


def _merge(arr: list, aux: list, lo: int, mid: int, hi: int):

    # Copy to auxiliary array
    aux[lo:hi+1] = arr[lo:hi+1]

    # Zipper merge
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

    if l_ind <= mid:
        arr[curr:hi+1] = aux[l_ind:mid+1]
    elif r_ind <= hi:
        arr[curr:hi+1] = aux[r_ind:hi+1]