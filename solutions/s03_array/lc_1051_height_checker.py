# Title: 1051. Height Checker
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/height-checker/
# Time: O(nlogn)
# Space: O(n) 


from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Approach: Sort and compare
        - Make a sorted copy of heights (expected order).
        - Count how many indices differ from the original.
        """
        expected = sorted(heights)
        mismatches = 0
        for a, b in zip(heights, expected):
            if a != b:
                mismatches += 1
        return mismatches

if __name__ == "__main__":
    sol = Solution()

    assert sol.heightChecker([1,1,4,2,1,3]) == 3
    assert sol.heightChecker([5,1,2,3,4]) == 5
    assert sol.heightChecker([1,2,3,4,5]) == 0
    assert sol.heightChecker([1]) == 0
    assert sol.heightChecker([2,2,2]) == 0

    print("Quick tests passed")
