# Title: 1046. Last Stone Weight
# Difficulty: Easy
# Tags: Heap
# Link: https://leetcode.com/problems/last-stone-weight/
# Time: O(nlogn)
# Space: O(n)

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Use max-heap (store negative values).
        Each round: pop two heaviest, smash, push remainder if any.
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # heaviest
            x = -heapq.heappop(heap)  # 2nd heaviest
            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0


if __name__ == "__main__":
    sol = Solution()

    assert sol.lastStoneWeight([2,7,4,1,8,1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    assert sol.lastStoneWeight([9,3,2,10]) == 0  # 10-9=1, 3-2=1, 1-1=0
    
    print("Quick tests passed")
