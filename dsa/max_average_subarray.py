# Question: Maximum average subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:
# Input: nums = [5], k = 1
# Output: 5.00000

def findMaxAverage(nums: list[int], k: int) -> float:
    # Initialize the sum of first k elements
    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    # Slide the window through the array
    for i in range(k, len(nums)):
        # Add new element and remove first element of previous window
        curr_sum = curr_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)

    # Return the maximum average
    return max_sum / k