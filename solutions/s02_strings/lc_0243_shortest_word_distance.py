# Title: 0243. Shortest Word Distance
# Difficulty: Easy
# Tags: Array, String
# Link: https://leetcode.com/problems/shortest-word-distance/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        """
        One-pass scan:
        - Track last seen positions of word1 and word2.
        - Update min distance whenever both have been seen.
        """
        i1 = i2 = -1
        res = float("inf")

        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
                if i2 != -1:
                    res = min(res, abs(i1 - i2))
            elif w == word2:
                i2 = i
                if i1 != -1:
                    res = min(res, abs(i1 - i2))

        return res
        

if __name__ == "__main__":
    sol = Solution()

    assert sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice") == 3
    assert sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding") == 1
    assert sol.shortestDistance(["a","b","c","d","a"], "a", "d") == 1
    assert sol.shortestDistance(["a","c","a","b"], "a", "b") == 1

    print("Quick tests passed")
