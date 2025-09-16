# Title: 0448. Find All Numbers Disappeared in an Array
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Approach:
        - For each num, mark index abs(num)-1 as negative (to indicate presence).
        - At the end, indices with positive values correspond to missing numbers.
        """
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i+1 for i, val in enumerate(nums) if val > 0]


if __name__ == "__main__":
    sol = Solution()

    assert sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6]
    assert sol.findDisappearedNumbers([1,1]) == [2]
    assert sol.findDisappearedNumbers([2,2]) == [1]
    assert sol.findDisappearedNumbers([1,2,3,4,5]) == []
    assert sol.findDisappearedNumbers([5,4,3,2,1]) == []

    print("Quick tests passed")

