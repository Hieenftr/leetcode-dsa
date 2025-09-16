# Title: 0238. Product of Array Except Self
# Difficulty: Medium
# Tags: Array
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach:
        - res[i] = product of all elements to the left of i * product of all elements to the right of i
        - First pass: compute prefix product into res[i]
        - Second pass: multiply suffix product into res[i]
        """
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert sol.productExceptSelf([2,3]) == [3,2]
    assert sol.productExceptSelf([5]) == [1]  # edge case
    assert sol.productExceptSelf([0,0]) == [0,0]
    
    print("Quick tests passed")
