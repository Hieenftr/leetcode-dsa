# Title: 695. Max Area of Island
# Difficulty: Medium
# Tags: Grid, DFS
# Link: https://leetcode.com/problems/max-area-of-island/
# Time: O(m * n)
# Space: O(m * n) recursion stack

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        - Traverse all cells.
        - When finding land (1), run DFS to explore the whole island.
        - DFS counts area by marking visited cells (turn 1 -> 0).
        - Keep track of maximum area found.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 0  # mark visited
            area = 1
            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)
            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
