# Title: 560. Subarray Sum Equals K
# Difficulty: Medium
# Tags: Array, Prefix Sum, HashMap
# Link: https://leetcode.com/problems/subarray-sum-equals-k/
# Time: O(n)
# Space: O(n)

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Prefix sum + hashmap:
        - cur_sum: running sum
        - For each num, check how many times (cur_sum - k) has appeared.
        - That count is number of valid subarrays ending here.
        """
        count = defaultdict(int)
        count[0] = 1
        res = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num
            res += count[cur_sum - k]
            count[cur_sum] += 1
        return res

if __name__ == "__main__":
    sol = Solution()

    assert sol.subarraySum([1, 1, 1], 2) == 2
    assert sol.subarraySum([1, 2, 3], 3) == 2
    assert sol.subarraySum([1], 0) == 0
    assert sol.subarraySum([1, -1, 0], 0) == 3
    assert sol.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4

    print("Quick tests passed")