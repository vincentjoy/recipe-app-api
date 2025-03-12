# Question - Rotate Array
# Leetcode link - https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150

def rotate(nums, k):
    """
    Rotate the array to the right by k steps.

    Args:
        nums: List[int] - The array to be rotated
        k: int - Number of steps to rotate to the right

    Returns:
        None - Modifies nums in-place
    """
    n = len(nums)
    # Handle edge cases
    if n <= 1 or k % n == 0:
        return

    # Get effective rotation amount (in case k > n)
    k = k % n

    # Solution using the three-step reversal approach
    # 1. Reverse the entire array
    # 2. Reverse first 'k' elements
    # 3. Reverse remaining elements

    # Helper function to reverse a portion of the array
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Reverse the entire array
    reverse(nums, 0, n - 1)

    # Reverse first 'k' elements
    reverse(nums, 0, k - 1)

    # Reverse remaining elements
    reverse(nums, k, n - 1)


# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]