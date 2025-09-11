# Title: 1614. Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Tags: String, Stack
# Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Time: O(n)
# Space: O(1)

class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Scan once, track current depth and the maximum seen.
        Increment on '(' and decrement on ')'.
        Ignore non-parenthesis characters.
        """
        depth = 0
        ans = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > ans:
                    ans = depth
            elif ch == ')':
                depth -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert sol.maxDepth("(1)+((2))+(((3)))") == 3
    assert sol.maxDepth("1+(2*3)/(2-1)") == 1
    assert sol.maxDepth("1") == 0
    assert sol.maxDepth("") == 0
    assert sol.maxDepth("((a)+(b))") == 2
    assert sol.maxDepth("((()))") == 3

    print("Quick tests passed")
