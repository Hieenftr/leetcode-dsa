# Title: 130. Surrounded Regions
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/surrounded-regions/
# Time: O(m*n)
# Space: O(m*n)

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        - 'O' connected to the border cannot be captured.
        - Step 1: DFS from all border 'O' and mark them as 'E' (escape).
        - Step 2: Traverse whole board:
            - Convert remaining 'O' -> 'X' (captured).
            - Convert 'E' back -> 'O'.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'  # mark as escaped
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        # mark border-connected 'O'
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols-1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows-1, c)

        # flip captured 'O' to 'X', restore 'E' to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'


if __name__ == "__main__":
    sol = Solution()

    board1 = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ]
    sol.solve(board1)
    assert board1 == [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ]

    board2 = [["X"]]
    sol.solve(board2)
    assert board2 == [["X"]]

    board3 = [
        ["O","O"],
        ["O","O"]
    ]
    sol.solve(board3)
    assert board3 == [
        ["O","O"],
        ["O","O"]
    ]  # all border-connected, none captured

    print("Quick tests passed")
