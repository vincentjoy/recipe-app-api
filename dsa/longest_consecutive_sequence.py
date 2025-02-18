# Question: Find the Longest Consecutive Sequence

# Given an unsorted array of integers, find the length of the longest consecutive sequence of numbers.

# Example 1 :
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive sequence is `[1, 2, 3, 4]`, so the length is `4`.

# Example 2:
# Input: [9, 1, 3, 10, 2, 4, 20]
# Output: 4
# Explanation: The longest consecutive sequence is `[1, 2, 3, 4]`, so the length is `4`.

def longest_consecutive(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    longest_length = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            longest_length = max(longest_length, current_length)

    return longest_length