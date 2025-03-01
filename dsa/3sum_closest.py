# Question - 3sum Closest point

# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

def threeSumClosest(nums, target):
    """
    Find three integers in nums such that the sum is closest to target.

    Args:
        nums: List[int] - Array of integers
        target: int - Target sum

    Returns:
        int - Sum of the three integers closest to target
    """
    # Sort the array for the two-pointer approach
    nums.sort()
    n = len(nums)

    # Initialize with the sum of first three elements
    closest_sum = nums[0] + nums[1] + nums[2]

    # Iterate through the array, fixing the first element
    for i in range(n - 2):
        # Skip duplicates for optimization
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Two pointers for the remaining elements
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            # If we found an exact match, return immediately
            if current_sum == target:
                return target

            # Update closest_sum if current_sum is closer to target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Adjust pointers based on comparison with target
            if current_sum < target:
                left += 1
            else:
                right -= 1

    return closest_sum

# Example usage:
nums1 = [-1, 2, 1, -4]
target1 = 1
print(f"The sum closest to {target1} is: {threeSumClosest(nums1, target1)}")  # Output: 2

nums2 = [0, 1, 2]
target2 = 3
print(f"The sum closest to {target2} is: {threeSumClosest(nums2, target2)}")  # Output: 3