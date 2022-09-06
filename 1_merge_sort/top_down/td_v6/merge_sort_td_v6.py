def merge_sort(nums):
    if len(nums) > 1: # Only do anything if this sublist is at least 2 elements long
        pivot = len(nums)//2
        left = merge_sort(nums[:pivot])
        right = merge_sort(nums[pivot:])
        return _merge(left, right)
    return nums


def _merge(left, right):

    ret = [] # List to be returned
    l_ind = r_ind = 0 # Traversal indices left and right

    # Zipper merge
    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] < right[r_ind]:
            ret.append(left[l_ind])
            l_ind += 1
        else:
            ret.append(right[r_ind])
            r_ind += 1

    # The if checks here seemed superfluous previously, but I've added them back in because those if checks are so much less expensive than an extend operation that does nothing.
    if l_ind < len(left):
        ret.extend(left[l_ind:])
    elif r_ind < len(right):
        ret.extend(right[r_ind:])

    return ret