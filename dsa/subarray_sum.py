# Question: Subarray Sum Equals K
# Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.

# Example 1:
# Input:
# let nums = [1, 1, 1]
# let k = 2
# Output: 2
# The subarrays [1,1] at indices (0,1) and (1,2) sum up to k = 2.

# Example 2:
# Input:
# let nums = [3, 4, 7, 2, -3, 1, 4, 2]
# let k = 7
# Output: 4
# The subarrays that sum up to 7 are: [7], [3, 4], [4, 7, 2, -3], [1, 4, 2]

def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_sums = {0: 1} # Base case: sum 0 exists once (empty subarray)

    for num in nums:
        prefix_sum += num # Update prefix sum

        # Check if (prefixSum - k) exists in dictionary
        if prefix_sum - k in prefix_sums:
            count += prefix_sums[prefix_sum - k]

        # Store/update occurrences of the current prefixSum
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

    return count