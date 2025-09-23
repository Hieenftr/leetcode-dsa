# Title: 0921. Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Time: O(n)
# Space: O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0   # open '(' waiting for ')'
        add = 0       # number of insertions needed

        for ch in s:
            if ch == '(':
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    balance -= 1  # match with a previous '('
                else:
                    add += 1      # need one '(' before this ')'

        return add + balance


if __name__ == "__main__":
    sol = Solution()

    assert sol.minAddToMakeValid("())") == 1
    assert sol.minAddToMakeValid("(((") == 3
    assert sol.minAddToMakeValid("()") == 0
    assert sol.minAddToMakeValid("()))((") == 4

    print("Quick tests passed")
