# Title: 442. Find All Duplicates in an Array
# Difficulty: Medium
# Tags: Array
# Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Approach:
        - Iterate over each number.
        - Use its absolute value to find an index.
        - If the number at that index is positive, mark it negative (first visit).
        - If it's already negative, that means we've seen this number before -> duplicate.
        """
        res = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(abs(num))
            else:
                nums[idx] = -nums[idx]

        return res

if __name__ == "__main__":
    sol = Solution()

    assert sol.findDuplicates([4,3,2,7,8,2,3,1]) == [2,3]
    assert sol.findDuplicates([1,1,2]) == [1]
    assert sol.findDuplicates([1]) == []

    print("Quick tests passed")