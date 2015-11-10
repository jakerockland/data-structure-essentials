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


# bubble sort is an O(n^2) algorithm, O(n) at best
def bubble_sort(items):
    size = len(items)

    for i in range(size):
        sorted = True
        for j in range(size-1):
            if items[j] > items[j+1]:
                swap(items, j, j+1)
                sorted = False
        if sorted:
            return # items have finished sorting

    return # items are sorted


# insertion sort is an O(n^2) algorithm, O(n) at best
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


# quicksort is an O(n*log(n)) algorithm, O(n^2) at worst
def quick_sort(items, low = None, high = None):
    # initial method call without optional variables provided
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1

    # if there are one or zero items, partition is already sorted
    if low >= high:
        return # items are sorted

    # partition the data items, index returned is highest item in low partition
    mid = partition_items(items, low, high)

    # recursively sort low partition and high partition
    quick_sort(items, low, mid)
    quick_sort(items, mid + 1, high)

    return # items are sorted

# helper method to partition items for quicksort algorithm
def partition_items(items, low, high):
    # select middle element as pivot point to partition
    mid = low + (high - low) / 2
    pivot = items[mid]

    done = False
    while not done:
        # increment low point while pivot is greater than low item
        while pivot > items[low]:
            low += 1

        # decrement high point while pivot is less than high item
        while pivot < items[high]:
            high -= 1

        if low >= high:
            # if zero or one items remaining, all items have been partitioned
            done = True
        else:
            # swap low and right numbers and update low and high indices
            swap(items, low, high)
            low += 1
            high -= 1

    return high # returns highest index of low partition


# merge sort is an O(n*log(n)) algorithm
def merge_sort(items, first = None, last = None):
    if first is None:
        first = 0
    if last is None:
        last = len(items) - 1

    if first < last:
        mid = (first + last) / 2

        # recursively sort left and right partitions
        merge_sort(items, first, mid)
        merge_sort(items, mid + 1, last)

        # merge partitions together
        merge_items(items, first, mid, last)

    return # items are sorted

# helper method to merge partitions for mergesort algorithm
def merge_items(items, first, mid, last):
    # temporary array for merged items
    merged_items = [None] * (last - first + 1)

    # variables for keeping track of merged index and partition locations
    index = 0
    left = first
    right = mid + 1

    # add smallest element from left or right partition to merged items
    while left <= mid and right <= last:
        if items[right] > items[left]:
            merged_items[index] = items[left]
            left += 1
        else:
            merged_items[index] = items[right]
            right += 1
        index += 1

    # add remaining items to merged items if left partition is not empty
    while left <= mid:
        merged_items[index] = items[left]
        left += 1
        index += 1

    # add remaining items to merged items if right partition is not empty
    while right <= last:
        merged_items[index] = items[right]
        right += 1
        index += 1

    # copy merged items back to items list
    for index in range(len(merged_items)):
        items[first + index] = merged_items[index]

    return
