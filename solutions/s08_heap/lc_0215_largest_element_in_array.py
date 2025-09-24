# Title: 0215. Kth Largest Element in an Array
# Difficulty: Medium
# Tags: Heap
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Time: O(nlogk)
# Space: O(k)

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Maintain a min-heap of size k.
        At the end, the root of the heap is the kth largest element.
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1

    print("Quick tests passed")
