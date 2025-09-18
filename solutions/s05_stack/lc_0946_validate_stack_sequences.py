# Title: 0946. Validate Stack Sequences
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/validate-stack-sequences/
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Simulate stack operations:
        - Push from 'pushed'.
        - Pop whenever top matches 'popped[j]'.
        - At the end, stack should be empty if valid.
        """
        stack = []
        j = 0  # index in popped

        for x in pushed:
            stack.append(x)
            # Pop while top of stack matches next in popped
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return not stack


if __name__ == "__main__":
    sol = Solution()

    assert sol.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]) is True
    assert sol.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]) is False
    assert sol.validateStackSequences([2,1,0], [1,2,0]) is True

    print("Quick tests passed")
