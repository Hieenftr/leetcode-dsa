# Title: 1. Two Sum
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/two-sum/
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach:
        - Use a hash map to store previously seen numbers and their indices.
        - For each number, check if (target - number) already exists in the map.
        - If yes, return indices of the two numbers.
        """

        seen = {}  # {num(key):index i (value)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    

if __name__ == "__main__":
    sol = Solution()

    assert sol.twoSum([2,7,11,15], 9) == [0,1]
    assert sol.twoSum([3,2,4], 6) == [1,2]
    assert sol.twoSum([3,3], 6) == [0,1]

    print("Quick tests passed")

