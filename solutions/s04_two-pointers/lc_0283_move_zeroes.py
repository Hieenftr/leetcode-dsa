# Title: 0283. Move Zeroes
# Difficulty: Easy
# Tags: Two Pointers
# Link: https://leetcode.com/problems/move-zeroes/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        - Use 'pos' to track the place to put next non-zero.
        - Iterate over nums:
            - If non-zero -> move it to nums[pos], pos++.
        - After loop, fill remaining with 0.
        """
        n = len(nums)
        pos = 0

        # Move all non-zeros to the front
        for i in range(n):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        # Fill the rest with 0
        for i in range(pos, n):
            nums[i] = 0


if __name__ == "__main__":
    sol = Solution()

    arr1 = [0,1,0,3,12]
    sol.moveZeroes(arr1)
    assert arr1 == [1,3,12,0,0]

    arr2 = [0]
    sol.moveZeroes(arr2)
    assert arr2 == [0]

    arr3 = [1,2,3]
    sol.moveZeroes(arr3)
    assert arr3 == [1,2,3]

    print("Quick tests passed")
