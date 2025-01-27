# Find Smallest Missing Positive Number

# Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.

# Input: arr[] = {2, -3, 4, 1, 1, 7}
# Output: 3
# Explanation: 3 is the smallest positive number missing from the array.

#Input: arr[] = {5, 3, 2, 5, 1}
#Output: 4
#Explanation: 4 is the smallest positive number missing from the array.

#Input: arr[] = {-8, 0, -1, -4, -3}
#Output: 1
#Explanation: 1 is the smallest positive number missing from the array.

def find_smallest_missing_positive(arr):
    n = len(arr)

    # Step 1: Place each number at its correct position
    i = 0
    while i < n:
        # correct position for number k is k-1 index
        correct_pos = arr[i] - 1

        # Check if current number is positive and within range
        # and not already at its correct position
        if 0 < arr[i] <= n and arr[i] != arr[correct_pos]:
            # Swap numbers
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
        else:
            i += 1

    # Step 2: Find first number that's not at correct position
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    # If all numbers from 1 to n exist
    return n + 1

# Example usage and test cases
test_cases = [
    [2, 3, -7, 6, 8, 1, -10, 15],
    [1, 1, 0, -1, -2],
    [7, 8, 9, 11, 12],
    [1, 2, 3, 4, 5]
]

for arr in test_cases:
    result = find_smallest_missing_positive(arr.copy())
    print(f"Input: {arr}")
    print(f"Smallest missing positive: {result}\n")