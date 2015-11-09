# Implementations of various searching algorithms
# By: Jacob Rockland

# Linear search is an O(n) search algorithm
def linear_search(numbers, key):
    for number in numbers:
        if number == key:
            return number

    return None # element not found

# Binary search is an O(log(n)) search algorithm
def binary_search(numbers, key):
    low = 0
    high = len(numbers) - 1
    mid = 0

    while high >= low:
        mid = (high + low) / 2
        if key > numbers[mid]:
            low = mid + 1
        elif key < numbers[mid]:
            high = mid - 1
        else:
            return numbers[mid]

    return None # element not found
