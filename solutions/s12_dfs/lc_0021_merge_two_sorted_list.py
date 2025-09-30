# Title: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Tags: Linked List, DFS
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Time: O(m+n)
# Space: O(m+n)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        - Compare heads of list1 and list2.
        - Smaller node becomes head; recursively merge the rest.
        - Base cases: if one list is empty, return the other.
        """
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

