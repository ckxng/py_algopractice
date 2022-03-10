def quicksort(ary):
    return quicksort_pythonic(ary)


def quicksort_pythonic(ary):
    if ary is not None:
        pivot = ary[0]
        low = [i for i in ary[1:] if i <= pivot]
        high = [i for i in ary[1:] if i > pivot]
        return quicksort_pythonic(low) + [pivot] + quicksort_pythonic(high)
    else:
        return ary


def quicksort_traditional(ary, low=0, high=None):
    if high is None:
        high = len(ary) - 1

    def _partition(ary, low, high):
        # set the pivot index to left of the sortable range, which is
        # so far the only position guaranteed to be less than the pivot value,
        # and therefore the current pivot index
        pi = low - 1

        # this is the value we will pivot around.  the final pi will be
        # equal to `low + (the number of values <= pivot)`
        pivot = ary[high]

        # visit every element of the array starting after the pi
        # (which is the whole array)
        for i in range(low, high + 1):
            # for every element <= pivot, increase pi and swap that value with
            # ary[pi], filling in the beginning of the array one swap at a time
            if ary[i] <= pivot:
                pi += 1
                ary[i], ary[pi] = ary[pi], ary[i]

        return ary, pi

    def _quicksort_traditional(ary, low, high):
        # sort if low is still less than high
        # low and high will converge during recursion
        if low < high:
            # partition the array and return the index where the partition occurs
            ary, pi = _partition(ary, low, high)

            # sort the low and high partitions
            ary = _quicksort_traditional(ary, low, pi - 1)
            ary = _quicksort_traditional(ary, pi + 1, high)

        # else pass, nothing to sort

        return ary

    return _quicksort_traditional(ary, low, high)
