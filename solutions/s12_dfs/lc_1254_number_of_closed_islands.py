# Title: 1254. Number of Closed Islands
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/number-of-closed-islands/
# Time: O(m*n)
# Space: O(m*n)

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        - 0 = land, 1 = water.
        - A closed island is a 0-region not touching the border.
        - For each unvisited land cell, DFS flood it to water (mark 0 -> 1)
          and return whether this region stays inside bounds.
        - Count regions where DFS returns True.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            # If out of bounds -> means it touches border (not closed)
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # If water, this path is fine (doesn't break closedness)
            if grid[r][c] == 1:
                return True

            # Mark visited (turn land -> water)
            grid[r][c] = 1

            up    = dfs(r-1, c)
            down  = dfs(r+1, c)
            left  = dfs(r, c-1)
            right = dfs(r, c+1)

            # This region is closed only if all four directions stayed inside
            return up and down and left and right

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1
        return count

