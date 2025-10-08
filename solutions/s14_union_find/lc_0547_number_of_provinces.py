# Title: 547. Number of Provinces
# Difficulty: Medium
# Tags: Union Find
# Link: https://leetcode.com/problems/number-of-provinces/
# Time: O(n^2)
# Space: O(n)

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        - Each city = node; if isConnected[i][j] == 1, union(i, j).
        - The number of unique roots after unions = number of provinces.
        """
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        # Count unique roots
        roots = {uf.find(i) for i in range(n)}
        return len(roots)


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    isConnected = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    assert sol.findCircleNum(isConnected) == 2

    # Example 2
    isConnected = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert sol.findCircleNum(isConnected) == 3

    # Example 3
    isConnected = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
    assert sol.findCircleNum(isConnected) == 1

    print("Quick tests passed")
