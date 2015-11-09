# Implementations of various searching algorithms
# By: Jacob Rockland

# linear search is an O(n) search algorithm
def linear_search(items, key):
    for item in items:
        if item == key:
            return item

    return None # element not found

# binary search is an O(log(n)) search algorithm
def binary_search(items, key):
    low = 0
    high = len(items) - 1
    mid = 0

    while high >= low:
        mid = (high + low) / 2
        if key > items[mid]:
            low = mid + 1
        elif key < items[mid]:
            high = mid - 1
        else:
            return items[mid]

    return None # element not found
