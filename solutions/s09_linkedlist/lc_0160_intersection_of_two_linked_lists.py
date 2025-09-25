# Title: 160. Intersection of Two Linked Lists
# Difficulty: Easy
# Tags: Linked List
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Time: O(n)
# Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the node at which the intersection of two singly linked lists begins.
        If no intersection, return None.

        Approach (two pointers):
        - Use two pointers pA, pB starting at headA, headB.
        - Move each forward one step.
        - When a pointer reaches the end, redirect it to the other list's head.
        - If the lists intersect, pointers will meet at the intersection.
        - If not, both will become None at the same time.
        """
        if not headA or not headB:
            return None

        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
