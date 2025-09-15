# Title: 268. Missing Number
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/missing-number/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Approach: Gauss sum
        - Expected sum for 0..n is n*(n+1)//2
        - Missing = expected_sum - actual_sum
        """
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


if __name__ == "__main__":
    sol = Solution()

    assert sol.missingNumber([3,0,1]) == 2
    assert sol.missingNumber([0,1]) == 2
    assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert sol.missingNumber([0]) == 1
    assert sol.missingNumber([1]) == 0

    print("Quick tests passed")