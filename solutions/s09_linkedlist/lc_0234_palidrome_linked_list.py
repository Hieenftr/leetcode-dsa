# Title: 234. Palindrome Linked List
# Difficulty: Easy
# Tags: Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Time: O(n)
# Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach:
        1. Use slow/fast pointers to find the middle.
        2. Reverse the second half of the list.
        3. Compare the first and second halves node by node.
        4. (Optional) Restore the list by reversing again.
        """
        if not head or not head.next:
            return True

        # Step 1: find middle (slow at middle)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        # Step 3: compare halves
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
