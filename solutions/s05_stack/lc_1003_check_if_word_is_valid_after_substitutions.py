# Title: 1003. Check If Word Is Valid After Substitutions
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Time: O(n)
# Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach:
        - Traverse characters and push to stack.
        - If last 3 chars in stack form "abc", pop them out.
        - At the end, stack should be empty if valid.
        """
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 3 and "".join(stack[-3:]) == "abc":
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid("aabcbc") is True
    assert sol.isValid("abcabcababcc") is True
    assert sol.isValid("abccba") is False
    assert sol.isValid("cababc") is False

    print("Quick tests passed")
