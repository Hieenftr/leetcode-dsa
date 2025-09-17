# Title: 0011. Container With Most Water
# Difficulty: Medium
# Tags: Two Pointers
# Link: https://leetcode.com/problems/container-with-most-water/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers:
        - Start with left=0, right=n-1.
        - Compute area = min(height[left], height[right]) * (right-left).
        - Move the pointer at the shorter line inward.
        - Keep track of max area.
        """
        left, right = 0, len(height) - 1
        res = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            res = max(res, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert sol.maxArea([1,1]) == 1
    assert sol.maxArea([4,3,2,1,4]) == 16
    assert sol.maxArea([1,2,1]) == 2

    print("Quick tests passed")
