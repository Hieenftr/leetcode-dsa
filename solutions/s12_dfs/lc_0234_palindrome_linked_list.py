# Title: 234. Palindrome Linked List
# Difficulty: Easy
# Tags: Linked List, DFS
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Time: O(n)
# Space: O(n)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        - Use a pointer `front` starting at head.
        - Recursively reach the end of list (backtracking acts as reverse traversal).
        - On unwind, compare current node with `front`, then move `front` forward.
        - If all match, it's a palindrome.
        """
        self.front = head

        def dfs(node: Optional[ListNode]) -> bool:
            if not node:
                return True
            if not dfs(node.next):
                return False
            if self.front.val != node.val:
                return False
            self.front = self.front.next
            return True

        return dfs(head)


