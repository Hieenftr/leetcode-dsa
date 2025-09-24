# Title: 0659. Split Array into Consecutive Subsequences
# Difficulty: Medium
# Tags: Heap
# Link: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Time: O(nlogn)
# Space: O(n)

from typing import List
from collections import defaultdict
import heapq

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        - heaps[v]: min-heap of lengths of subsequences ending at value v.
        - For each x:
            - If there is a subseq ending at x-1, extend its SHORTEST one.
            - Else start a new subseq of length 1 at x.
        - At the end, ensure every subseq length >= 3.
        """
        heaps = defaultdict(list)  # end_value -> min-heap of lengths

        for x in nums:  # nums is given sorted
            if heaps[x - 1]:
                L = heapq.heappop(heaps[x - 1])   # extend the SHORTEST chain
                heapq.heappush(heaps[x], L + 1)
            else:
                heapq.heappush(heaps[x], 1)       # start new chain

        # all chains must have length >= 3
        for h in heaps.values():
            if h and h[0] < 3:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    
    assert sol.isPossible([1,2,3,3,4,5]) is True            # [1,2,3] and [3,4,5]
    assert sol.isPossible([1,2,3,3,4,4,5,5]) is True        # [1,2,3,4,5] and [3,4,5]
    assert sol.isPossible([1,2,3,4,4,5]) is False           # leftover length<3
    assert sol.isPossible([1,2,3,4,5,6]) is True            # [1,2,3] and [4,5,6]

    print("Quick tests passed")
