# Title: Kth Largest Element In An Array
# Time: O(n log k)  |  Space: O(k)
# Tags: Array, Heap, Quickselect

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        if not nums:
            return 0

        for i in nums:
            heapq.heappush(heap, i)
            if len(heap) > k: 
                heapq.heappop(heap)
            
        return heapq.heappop(heap)

####

