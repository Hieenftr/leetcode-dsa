# Title: 994. Rotting Oranges
# Difficulty: Medium
# Tags: BFS
# Link: https://leetcode.com/problems/rotting-oranges/
# Time: O(m*n)
# Space: O(m*n)

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        - Put all rotten oranges into the queue at minute = 0.
        - Each minute, rot their fresh neighbors.
        - Track how many fresh oranges remain.
        - If fresh == 0 → return minutes, else → return -1.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Collect initial rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # BFS to rot fresh oranges
        while queue:
            r, c, t = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
                    minutes = t + 1

        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid = [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]
    assert sol.orangesRotting(grid) == 4

    # Example 2
    grid = [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ]
    assert sol.orangesRotting(grid) == -1

    # Example 3
    grid = [
        [0,2]
    ]
    assert sol.orangesRotting(grid) == 0

    print("Quick tests passed")
