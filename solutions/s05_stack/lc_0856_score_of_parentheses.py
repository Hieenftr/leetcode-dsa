# Title: 0856. Score of Parentheses
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/score-of-parentheses/
# Time: O(n)
# Space: O(n)

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Approach:
        - Use stack to store scores.
        - '(' -> push 0
        - ')' -> pop top v:
            * if v==0 -> push 1
            * else -> push 2*v
        - If stack has multiple values, sum them up.
        """
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:  # ')'
                v = stack.pop()
                if v == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * v
        return stack.pop()


if __name__ == "__main__":
    sol = Solution()

    assert sol.scoreOfParentheses("()") == 1
    assert sol.scoreOfParentheses("(())") == 2
    assert sol.scoreOfParentheses("()()") == 2
    assert sol.scoreOfParentheses("(()(()))") == 6

    print("Quick tests passed")
