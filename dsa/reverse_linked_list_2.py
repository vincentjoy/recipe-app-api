# Question - Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # If list is empty or no reversal needed
        if not head or left == right:
            return head

        # Create a dummy node to handle edge cases (like reversing from first node)
        dummy = ListNode(0)
        dummy.next = head

        # Find the node just before reversal starts
        prev_left = dummy
        for _ in range(1, left):
            prev_left = prev_left.next

        # Current will be the first node to be reversed
        current = prev_left.next

        # Reverse the sublist from left to right
        for _ in range(right - left):
            temp = current.next  # The node to be moved
            current.next = temp.next  # Skip the node being moved

            # Insert temp at the beginning of the reversed portion
            temp.next = prev_left.next
            prev_left.next = temp

        return dummy.next