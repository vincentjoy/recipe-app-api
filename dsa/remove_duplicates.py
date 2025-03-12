# Question - Remove Duplicates from Sorted Array II
# Leetcode link - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

def removeDuplicates(nums):
    # Handle edge cases
    if len(nums) <= 2:
        return len(nums)

    # Keep track of the position where the next element should be placed
    insert_index = 2

    # Start from the third element (index 2)
    for i in range(2, len(nums)):
        # If the current element is different from the element two positions back
        if nums[i] != nums[insert_index - 2]:
            nums[insert_index] = nums[i]
            insert_index += 1

    return insert_index