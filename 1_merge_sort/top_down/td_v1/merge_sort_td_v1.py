def merge_sort(nums):
    # base case
    if len(nums) <= 1:
        return nums
    pivot = int(len(nums) / 2)
    left = merge_sort(nums[:pivot])
    right = merge_sort(nums[pivot:])
    return _merge(left, right)


def _merge(left, right):

    ret = [] # list to be returned
    l_ind = r_ind = 0 # traversal indices left and right

    # now do the zipper merge
    while l_ind < len(left) and r_ind < len(right):
        if left[l_ind] < right[r_ind]:
            ret.append(left[l_ind])
            l_ind += 1
        else:
            ret.append(right[r_ind])
            r_ind += 1

    # Note: these if checks are unnecessary. Will fix in td_v2
    if l_ind < len(left):
        ret.extend(left[l_ind:])
    if r_ind < len(right):
        ret.extend(right[r_ind:])
    return ret
