# Title: 48. Rotate Image
# Difficulty: Medium
# Tags: Array, Matrix
# Link: https://leetcode.com/problems/rotate-image/
# Time: O(n^2)
# Space: O(1)

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Approach:
        - Transpose the matrix (swap across diagonal).
        - Reverse each row.
        - In-place, so modify the original matrix.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

if __name__ == "__main__":
    sol = Solution()
    
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(m1)
    assert m1 == [[7,4,1],[8,5,2],[9,6,3]]

    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(m2)
    assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print("Quick tests passed")