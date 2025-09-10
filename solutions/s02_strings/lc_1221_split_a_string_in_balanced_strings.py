# Title: 1221. Split a String in Balanced Strings
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Time: O(n)
# Space: O(1)

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Greedy:
        - Maintain a running balance: L -> +1, R -> -1.
        - Every time balance hits 0, we found one balanced substring.
        """
        bal = 0
        ans = 0
        for ch in s:
            bal += 1 if ch == 'L' else -1
            if bal == 0:
                ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.balancedStringSplit("RLRRLLRLRL") == 4
    assert sol.balancedStringSplit("RLRRRLLRLL") == 2
    assert sol.balancedStringSplit("LLLLRRRR") == 1
    assert sol.balancedStringSplit("LR") == 1
    assert sol.balancedStringSplit("RL") == 1
    assert sol.balancedStringSplit("LRLR") == 2
    assert sol.balancedStringSplit("RRLL") == 1
    assert sol.balancedStringSplit("") == 0

    print("Quick tests passed")
