# Title: 20. Valid Parentheses
# Difficulty: Easy
# Tags: Stack, String
# Link: https://leetcode.com/problems/valid-parentheses/
# Time: O(n)
# Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach:
        - Use a stack to match opening and closing brackets.
        - Traverse string:
          * If char is an opening bracket → push to stack.
          * If char is a closing bracket → check if stack top is matching.
            - If match → pop stack.
            - If not → invalid.
        - At the end, if stack empty → valid, else invalid.
        
        Why it works:
        - Stack preserves the order of nested brackets.
        - Each bracket processed once → O(n).
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in mapping.values():  # opening
                stack.append(ch)
            elif ch in mapping:  # closing
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                # invalid character (should not happen in LeetCode)
                return False

        return not stack
