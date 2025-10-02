# Title: 1306. Jump Game III
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/jump-game-iii/
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        - From index i, you can jump to i + arr[i] or i - arr[i] (if in bounds).
        - Use a visited set to avoid infinite loops.
        - Return True if any reachable index has value 0.
        """
        n = len(arr)
        visited = [False] * n

        def dfs(i: int) -> bool:
            if i < 0 or i >= n or visited[i]:
                return False
            if arr[i] == 0:
                return True
            visited[i] = True
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr = [4,2,3,0,3,1,2]
    start = 5
    assert sol.canReach(arr, start) == True  # 5 -> 4 -> 0 (index 3)

    # Example 2
    arr = [4,2,3,0,3,1,2]
    start = 0
    assert sol.canReach(arr, start) == True

    # Example 3
    arr = [3,0,2,1,2]
    start = 2
    assert sol.canReach(arr, start) == False

    # Edge: start already at zero
    arr = [0]
    start = 0
    assert sol.canReach(arr, start) == True

    # Edge: cycles but no zero reachable
    arr = [1,1,1,1]
    start = 2
    assert sol.canReach(arr, start) == False

    print("Quick tests passed")
