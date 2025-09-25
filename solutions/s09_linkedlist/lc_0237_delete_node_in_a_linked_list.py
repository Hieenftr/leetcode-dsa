# Title: 237. Delete Node in a Linked List
# Difficulty: Medium
# Tags: Linked List
# Link: https://leetcode.com/problems/delete-node-in-a-linked-list/
# Time: O(1)
# Space: O(1)

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Delete a node in a singly-linked list, given only access to that node.
        - Copy value from node.next into node.
        - Skip node.next by re-linking pointers.
        """
        node.val = node.next.val
        node.next = node.next.next
