# Title: 1004. Max Consecutive Ones III
# Difficulty: Medium
# Tags: Two Pointers, Sliding Window
# Link: https://leetcode.com/problems/max-consecutive-ones-iii/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        - Expand right; count zeros in the window.
        - While zeros > k, move left to drop zeros.
        - Track the max window length.
        """
        left = 0
        zeros = 0
        best = 0

        for right, val in enumerate(nums):
            if val == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert sol.longestOnes([0,0,1,1,1,0,0], 0) == 3
    assert sol.longestOnes([1,1,1,1], 2) == 4
    assert sol.longestOnes([0,0,0,0], 2) == 2
    assert sol.longestOnes([1,0,1,0,1,0,1], 3) == 7

    print("Quick tests passed")
