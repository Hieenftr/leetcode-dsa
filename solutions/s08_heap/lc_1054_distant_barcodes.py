# Title: 1054. Distant Barcodes
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/distant-barcodes/
# Time: O(nlogn)
# Space: O(n)

from typing import List
from collections import Counter

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        Count frequencies, sort descending, then place numbers into
        even indices first, then odd indices to avoid adjacent equals.
        """
        n = len(barcodes)
        res = [0] * n

        # pairs: (value, count) sorted by count desc
        items = sorted(Counter(barcodes).items(), key=lambda x: -x[1])

        i = 0  # write pointer
        for val, cnt in items:
            for _ in range(cnt):
                if i >= n:
                    i = 1  # switch to odd indices
                res[i] = val
                i += 2
        return res


if __name__ == "__main__":
    sol = Solution()

    out1 = sol.rearrangeBarcodes([1,1,1,2,2,2])
    assert all(out1[i] != out1[i+1] for i in range(len(out1)-1))
    out2 = sol.rearrangeBarcodes([1,1,1,1,2,2,3,3])
    assert all(out2[i] != out2[i+1] for i in range(len(out2)-1))
    out3 = sol.rearrangeBarcodes([7,7,7,8,5,7,5,5,5,8])
    assert all(out3[i] != out3[i+1] for i in range(len(out3)-1))

    print("Quick tests passed")
