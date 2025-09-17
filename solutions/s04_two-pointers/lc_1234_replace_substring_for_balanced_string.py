# Title: 1234. Replace the Substring for Balanced String
# Difficulty: Medium
# Tags: Two Pointers, Sliding Window
# Link: https://leetcode.com/problems/replace-the-substring-for-balanced-string/
# Time: O(n)
# Space: O(1)

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        """
        - Count frequency of QWER.
        - Need to shrink window until outside chars are balanced (<= n/4).
        - Track min window length.
        """
        n = len(s)
        count = Counter(s)
        target = n // 4
        res = n

        left = 0
        for right, ch in enumerate(s):
            count[ch] -= 1
            # shrink window while the rest is balanced
            while left < n and all(count[c] <= target for c in "QWER"):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.balancedString("QWER") == 0
    assert sol.balancedString("QQWE") == 1
    assert sol.balancedString("QQQW") == 2
    assert sol.balancedString("QQQQ") == 3

    print("Quick tests passed")
