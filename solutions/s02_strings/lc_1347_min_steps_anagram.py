# Title: 1347. Minimum Number of Steps to Make Two Strings Anagram
# Difficulty: Medium
# Tags: String
# Link: https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
# Time: O(n)
# Space: O(1)   # since only lowercase English letters

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Count frequency differences between s and t.
        The number of steps = total positive deficits of t relative to s.
        """
        count_s = Counter(s)
        count_t = Counter(t)

        steps = 0
        for ch in count_s:
            if count_s[ch] > count_t[ch]:
                steps += count_s[ch] - count_t[ch]
        return steps


if __name__ == "__main__":
    sol = Solution()

    assert sol.minSteps("bab", "aba") == 1
    assert sol.minSteps("leetcode", "practice") == 5
    assert sol.minSteps("anagram", "mangaar") == 0
    assert sol.minSteps("xxyyzz", "xxyyzz") == 0
    assert sol.minSteps("friend", "family") == 4

    print("Quick tests passed")
