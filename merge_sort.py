def _merge_1(left: list, right: list) -> list:
    '''Merge sorted lists left and right into a new list and return that new
    list.'''

    result = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result += left[i:]
    result += right[j:]
    return result


def _mergesort_1(lst: list) -> list:
    '''Return a new list that is a sorted version of list lst.'''

    if len(lst) < 2:
        return lst
    else:
        middle = len(lst) // 2
        left = _mergesort_1(lst[:middle])
        right = _mergesort_1(lst[middle:])
    return _merge_1(left, right)


def mergesort_1(lst: list) -> None:
    '''Sort list lst.'''

    lst[:] = _mergesort_1(lst)
