# Implementations of various sorting algorithms
# By: Jacob Rockland

# selection sort is an O(n^2) algorithm
def selection_sort(items):
    size = len(items)

    for i in range(size):
        # index seperating sorted left hand side from unsorted right-hand side
        k = i

        # finds index of next smallest item in unsorted item
        for j in range(i+1,size):
            if items[j] < items[k]:
                k = j

        # swaps the current item with the smallest of unsorted items
        temp = items[i]
        items[i] = items[k]
        items[k] = temp

# insertion sort is an O(n^2) algorithm
def insertion_sort(items):
    size = len(items)

    for i in range(1,size):
        # index for finding what element to left of current where sorted
        j = i

        # insert current item 'i' into sorted part once, stopping in correct position
        while j > 0 and items[j-1] > items[j]:
            # swaps the current item with item to left of current item
            temp = items[j]
            items[j] = items[j-1]
            items[j-1] = temp
            j -= 1

# helper method to partition items for quick_sort method
# def partition_items(items, i, k):
