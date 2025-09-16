# Title: 1640. Check Array Formation Through Concatenation
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/check-array-formation-through-concatenation/
# Time: O(n*p)  # n = len(arr), p = len(pieces)
# Space: O(1)

from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        - Walk i over arr.
        - At each i, find a piece whose first element equals arr[i] by scanning pieces.
        - Then compare that piece sequentially against arr (advance i while matching).
        - If no piece starts with arr[i] or a mismatch occurs, return False.
        - If we consume the entire arr this way, return True.

        """
        i = 0
        n = len(arr)
        while i < n:
            found = False
            for piece in pieces:
                if piece and piece[0] == arr[i]:
                    found = True
                    for x in piece:
                        if i >= n or arr[i] != x:
                            return False
                        i += 1
                    break
            if not found:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.canFormArray([85], [[85]]) is True
    assert sol.canFormArray([15,88], [[88],[15]]) is True
    assert sol.canFormArray([49,18,16], [[16,18,49]]) is False
    assert sol.canFormArray([91,4,64,78], [[78],[4,64],[91]]) is True

    print("Quick tests passed")