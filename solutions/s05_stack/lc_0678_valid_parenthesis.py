
# Title: 0678. Valid Parenthesis String (Stack approach)
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/valid-parenthesis-string/
# Time: O(n)
# Space: O(n)

class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Approach:
        - stack_open: indices of '('
        - stack_star: indices of '*'
        - For ')': prefer to match '(' first, else use '*'.
        - After scan: match remaining '(' with '*' after them.
        """
        stack_open = []
        stack_star = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack_open.append(i)
            elif ch == '*':
                stack_star.append(i)
            else:  # ')'
                if stack_open:
                    stack_open.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False

        # Match remaining '(' with '*' that come after them
        while stack_open and stack_star:
            if stack_open[-1] < stack_star[-1]:
                stack_open.pop()
                stack_star.pop()
            else:
                return False

        return not stack_open


if __name__ == "__main__":
    sol = Solution()

    assert sol.checkValidString("()") is True
    assert sol.checkValidString("(*)") is True
    assert sol.checkValidString("(*))") is True
    assert sol.checkValidString("(*()") is True
    assert sol.checkValidString("(((******))") is True
    assert sol.checkValidString(")(") is False

    print("Quick tests passed")
