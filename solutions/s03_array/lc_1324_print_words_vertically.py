# Title: 1324. Print Words Vertically
# Difficulty: Medium
# Tags: String
# Link: https://leetcode.com/problems/print-words-vertically/
# Time: O(n * m) where n=#words, m=max word length
# Space: O(n * m)

from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        """
        Approach:
        - Split the string into words.
        - For each column index i (0..max_len-1):
          - Collect the ith character from each word if available, else ' '.
          - Strip trailing spaces before adding to result.
        """
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []

        for i in range(max_len):
            col = []
            for w in words:
                if i < len(w):
                    col.append(w[i])
                else:
                    col.append(" ")
            res.append("".join(col).rstrip())

        return res

if __name__ == "__main__":
    sol = Solution()

    assert sol.printVertically("HOW ARE YOU") == ["HAY","ORO","WEU"]
    assert sol.printVertically("TO BE OR NOT TO BE") == ["TBONTB","OEROOE","   T"]
    assert sol.printVertically("CONTEST IS COMING") == ["CIC","OSO","N M","T I","E N","S G","T"]

    print("Quick tests passed")
