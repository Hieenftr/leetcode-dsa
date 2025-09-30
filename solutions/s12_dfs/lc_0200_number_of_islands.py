# Title: 200. Number of Islands
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/number-of-islands/
# Time: O(m*n)
# Space: O(m*n)

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - Traverse all cells.
        - When encountering land '1', increment island count.
        - Use DFS to mark the entire connected land as visited (turn '1' -> '0').
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
                return
            grid[r][c] = '0'  # mark visited
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands

