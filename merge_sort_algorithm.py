# Learn Data Structures by Building the Merge Sort Algorithm:
# You'll learn how to interact with data structures by sorting a list of random numbers using the Merge Sort Algorithm.


def merge_sort(array):
    """Sorts an array 'array' (list) using the merge sort algorithm."""

    # Base case: if the length of the array is 0 or 1, it is already sorted.
    if len(array) <= 1:
        return

    # Split the array into two halves.
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursively sort each half.
    merge_sort(left_part)
    merge_sort(right_part)

    # Merge the sorted halves back together.
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Compare elements from both halves and merge them in sorted order.
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Add any remaining elements from the left half.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Add any remaining elements from the right half
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print("Sorted array: " + str(numbers))
