# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def binary_search(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:

        if target == num[left]:
            return left

        if target == num[right]:
            return right

        mid = (left + right) // 2

        if target == num[mid]:
            return mid

        if target < num[mid]:
            right = mid - 1

        if target > num[mid]:
            left = mid + 1

    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(binary_search(nums, target))