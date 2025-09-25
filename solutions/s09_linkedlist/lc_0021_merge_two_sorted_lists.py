# Title: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Tags: Linked List
# Link: https://leetcode.com/problems/merge-two-sorted-lists/
# Time: O(n)
# Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted list.
        - Use a dummy head to simplify construction.
        - Iterate through both lists, attaching the smaller node each time.
        - Append the remaining nodes after one list is exhausted.
        """
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
