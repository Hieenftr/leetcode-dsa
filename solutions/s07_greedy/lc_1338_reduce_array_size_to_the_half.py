# Title: 1338. Reduce Array Size to The Half
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/reduce-array-size-to-the-half/
# Time: O(nlogn)
# Space: O(n)

from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        Greedy:
        - Count frequencies.
        - Sort by descending frequency.
        - Pick largest until removed >= n/2.
        """
        freq = Counter(arr)
        counts = sorted(freq.values(), reverse=True)
        
        removed = 0
        res = 0
        half = len(arr) // 2
        
        for c in counts:
            removed += c
            res += 1
            if removed >= half:
                return res
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.minSetSize([3,3,3,3,5,5,5,2,2,7]) == 2
    assert sol.minSetSize([7,7,7,7,7,7]) == 1
    assert sol.minSetSize([1,9]) == 1
    assert sol.minSetSize([1000,1000,3,7]) == 1

    print("Quick tests passed")
