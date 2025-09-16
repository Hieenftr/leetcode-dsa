# Title: 0845. Longest Mountain in Array
# Difficulty: Medium
# Tags: Two Pointers
# Link: https://leetcode.com/problems/longest-mountain-in-array/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        """
        Two pointers:
        - Traverse to find a peak (arr[i-1] < arr[i] > arr[i+1]).
        - Expand left until the sequence stops increasing.
        - Expand right until the sequence stops decreasing.
        - Update max length.
        """
        n = len(arr)
        res = 0
        i = 1

        while i < n - 1:
            if arr[i-1] < arr[i] > arr[i+1]:
                l, r = i, i
                while l > 0 and arr[l-1] < arr[l]:
                    l -= 1
                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1
                res = max(res, r - l + 1)
                i = r
            else:
                i += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestMountain([2,1,4,7,3,2,5]) == 5
    assert sol.longestMountain([2,2,2]) == 0
    assert sol.longestMountain([1,2,3,4,5,4,3,2,1]) == 9
    assert sol.longestMountain([1,3,2]) == 3
    assert sol.longestMountain([1,2,3]) == 0
    assert sol.longestMountain([3,2,1]) == 0

    print("Quick tests passed")
