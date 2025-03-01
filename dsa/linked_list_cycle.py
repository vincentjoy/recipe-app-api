# Question - Linked list cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        # Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1 step
            fast = fast.next.next     # Move fast pointer by 2 steps

            if slow == fast:          # If they meet, there's a cycle
                return True

        return False                  # If fast reaches the end, no cycle