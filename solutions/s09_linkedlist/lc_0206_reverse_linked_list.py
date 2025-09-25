# Title: 206. Reverse Linked List
# Difficulty: Easy
# Tags: Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Time: O(n)
# Space: O(n)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly-linked list.
        - Use three pointers: prev, curr, next.
        - Traverse list and reverse links in-place.
        """
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
