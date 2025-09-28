# Title: 200. Number of Islands
# Difficulty: Medium
# Tags: Grid, BFS
# Link: https://leetcode.com/problems/number-of-islands/
# Time: O(m*n)
# Space: O(m*n)

from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        - Traverse all cells.
        - When finding land '1', increase count and BFS to sink the whole island.
        - Mark visited cells by turning '1' -> '0'.
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(sr: int, sc: int):
            queue = deque([(sr, sc)])
            grid[sr][sc] = '0'
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)

        return islands


if __name__ == "__main__":
    sol = Solution()

    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert sol.numIslands(grid1) == 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert sol.numIslands(grid2) == 3

    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    assert sol.numIslands(grid3) == 0

    print("Quick tests passed")
