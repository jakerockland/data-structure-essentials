# Implementations of various sorting algorithms
# By: Jacob Rockland

# helper method to swap two items of an array
def swap(items, i, j):
    temp = items[i]
    items[i] = items[j]
    items[j] = temp

# selection sort is an O(n^2) algorithm
def selection_sort(items):
    size = len(items)

    for i in range(size):
        # index seperating sorted left hand side from unsorted right-hand side
        k = i

        # finds index of next smallest item in unsorted item
        for j in range(i+1, size):
            if items[j] < items[k]:
                k = j

        # swaps the current item with the smallest of unsorted items
        swap(items, i, k)

    return # items are sorted

# bubble sort is an O(n^2) algorithm
def bubble_sort(items):
    pass # FIXME: Complete method
    return # items are sorted

# insertion sort is an O(n^2) algorithm at worst, O(n) at best
def insertion_sort(items):
    size = len(items)

    for i in range(1, size):
        # index for finding what element to left of current where sorted
        j = i

        # insert current item 'i' into sorted part once, stopping in correct position
        while j > 0 and items[j-1] > items[j]:
            # swaps the current item with item to left of current item
            swap(items, j, j-1)
            j -= 1

    return # items are sorted

# helper method to partition items for quicksort algorithm
def partition_items(items, left, right):
    # select middle element as pivot point to partition
    mid = left + (right - left) / 2
    pivot = items[mid]

    done = False
    while not done:
        # increment left point while pivot is greater than left item
        while pivot > items[left]:
            left += 1

        # decrement right point while pivot is less than right item
        while pivot < items[right]:
            right -= 1

        if left >= right:
            # if zero or one items remaining, all items have been partitioned
            done = True
        else:
            # swap left and right numbers and update left and right indices
            swap(items, left, right)
            left += 1
            right -= 1

    return right

# quicksort is at best an O(n*log(n)) sorting algorithm, at worst O(n^2)
def quick_sort(items, left = None, right = None):
    # base case method call
    if left is None:
        left = 0
    if right is None:
        right = len(items) - 1

    # if there are one or zero entries to sort, partition is already sorted
    if left >= right:
        return # items are sorted

    # partition the data items, index returned is highest item in left partition
    mid = partition_items(items, left, right)

    # recursively sort left partition and right partition
    quick_sort(items, left, mid)
    quick_sort(items, mid + 1, right)

    return # items are sorted
