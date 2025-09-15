# Title: 1572. Matrix Diagonal Sum
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/matrix-diagonal-sum/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Sum primary (i,i) and secondary (i,n-1-i) diagonals.
        If n is odd, subtract the center once because it was counted twice.
        """
        n = len(mat)
        total = 0
        for i in range(n):
            total += mat[i][i]                # primary diagonal
            total += mat[i][n - 1 - i]        # secondary diagonal
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]      # remove double-counted center
        return total



if __name__ == "__main__":
    sol = Solution()

    assert sol.diagonalSum([[1,2,3],
                          [4,5,6],
                          [7,8,9]]) == 25     # 1+5+9 + 3+5+7 - 5 = 25

    assert sol.diagonalSum([[1,1,1,1],
                          [1,1,1,1],
                          [1,1,1,1],
                          [1,1,1,1]]) == 8    # 4+4 diagonals, no center overlap

    assert sol.diagonalSum([[5]]) == 5          # single element

    print("Quick tests passed")