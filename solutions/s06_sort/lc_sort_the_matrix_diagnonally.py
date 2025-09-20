# Title: 1329. Sort the Matrix Diagonally
# Difficulty: Medium
# Tags: Sort
# Link: https://leetcode.com/problems/sort-the-matrix-diagonally/
# Time: O(mnlogk)
# Space: O(mn)

from typing import List
from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Group by key (r - c). Sort each diagonal then write back in order.
        """
        m, n = len(mat), len(mat[0])
        groups = defaultdict(list)

        # collect values per diagonal
        for r in range(m):
            for c in range(n):
                groups[r - c].append(mat[r][c])

        # sort ascending; for efficient pop, reverse to pop() from end
        for key in groups:
            groups[key].sort(reverse=True)

        # write back: take smallest remaining each time
        for r in range(m):
            for c in range(n):
                mat[r][c] = groups[r - c].pop()  # smallest

        return mat


if __name__ == "__main__":
    sol = Solution()

    assert sol.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
    assert sol.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]) == [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

    print("Quick tests passed")
