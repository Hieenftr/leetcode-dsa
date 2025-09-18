# Title: 1370. Increasing Decreasing String
# Difficulty: Easy
# Tags: Sort
# Link: https://leetcode.com/problems/increasing-decreasing-string/
# Time: O(n)
# Space: O(1)

from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        """
        Count characters, then repeatedly pick increasing then decreasing.
        """
        count = Counter(s)
        res = []
        while len(res) < len(s):
            # increasing
            for ch in sorted(count.keys()):
                if count[ch] > 0:
                    res.append(ch)
                    count[ch] -= 1
            # decreasing
            for ch in sorted(count.keys(), reverse=True):
                if count[ch] > 0:
                    res.append(ch)
                    count[ch] -= 1
        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    assert sol.sortString("aaaabbbbcccc") == "abccbaabccba"
    assert sol.sortString("rat") == "art"
    assert sol.sortString("leetcode") == "cdelotee"
    assert sol.sortString("ggggggg") == "ggggggg"
    assert sol.sortString("spo") == "ops"

    print("Quick tests passed")
