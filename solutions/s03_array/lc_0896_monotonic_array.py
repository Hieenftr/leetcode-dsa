# Title: 896. Monotonic Array
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/monotonic-array/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """
        Approach:
        - Track two flags: non-decreasing and non-increasing.
        - Traverse once and check each adjacent pair.
        """
        inc = True
        dec = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dec = False

        return inc or dec


if __name__ == "__main__":
    sol = Solution()

    assert sol.isMonotonic([1,2,2,3]) == True
    assert sol.isMonotonic([6,5,4,4]) == True
    assert sol.isMonotonic([1,3,2]) == False
    assert sol.isMonotonic([1,1,1]) == True
    assert sol.isMonotonic([10]) == True

    print("Quick tests passed")
