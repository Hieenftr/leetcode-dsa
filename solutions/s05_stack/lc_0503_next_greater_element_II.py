# Title: 0503. Next Greater Element II
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/next-greater-element-ii/
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Monotonic stack + circular array:
        - Traverse array twice (simulate circular).
        - While current num > nums[stack[-1]], pop and set result.
        - Push index during first round only.
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if i < n:
                stack.append(i)

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.nextGreaterElements([1,2,1]) == [2,-1,2]
    assert sol.nextGreaterElements([3,8,4,1,2]) == [8,-1,8,2,3]
    assert sol.nextGreaterElements([5,4,3,2,1]) == [-1,5,5,5,5]

    print("Quick tests passed")
