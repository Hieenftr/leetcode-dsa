# Title: 1502. Can Make Arithmetic Progression From Sequence
# Difficulty: Easy
# Tags: Sorting
# Link: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Time: O(nlogn)
# Space: O(1)

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        """
        Sort array, check constant difference between consecutive elements.
        """
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.canMakeArithmeticProgression([3,5,1]) is True
    assert sol.canMakeArithmeticProgression([1,2,4]) is False
    assert sol.canMakeArithmeticProgression([7,3,5,1]) is True
    
    print("Quick tests passed")
