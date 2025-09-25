# Title: 876. Middle of the Linked List
# Difficulty: Easy
# Tags: Linked List
# Link: https://leetcode.com/problems/middle-of-the-linked-list/
# Time: O(n)
# Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Return the middle node of a singly-linked list.
        If there are two middles (even length), return the SECOND middle.
        - Move 'slow' by 1 step and 'fast' by 2 steps.
        - When 'fast' reaches the end, 'slow' is at the middle.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
