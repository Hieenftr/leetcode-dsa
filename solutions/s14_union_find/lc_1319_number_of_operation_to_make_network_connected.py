# Title: 1319. Number of Operations to Make Network Connected
# Difficulty: Medium
# Tags: Union-Find
# Link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# Time: 
# Space: 

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of connected components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        self.count -= 1
        return True


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        Need at least (n-1) cables to connect n computers.
        If not enough edges, return -1.
        Otherwise, connect components via Union-Find.
        Answer = number_of_components - 1.
        """
        if len(connections) < n - 1:
            return -1

        uf = UnionFind(n)
        for u, v in connections:
            uf.union(u, v)

        return uf.count - 1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    n = 4
    connections = [[0,1],[0,2],[1,2]]
    assert sol.makeConnected(n, connections) == 1

    # Example 2
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
    assert sol.makeConnected(n, connections) == 2

    # Example 3
    n = 6
    connections = [[0,1],[0,2],[0,3],[1,2]]
    assert sol.makeConnected(n, connections) == -1

    # Already connected
    n = 3
    connections = [[0,1],[1,2]]
    assert sol.makeConnected(n, connections) == 0

    # Multiple components with spare edges
    n = 5
    connections = [[0,1],[2,3],[1,2],[3,4]]
    assert sol.makeConnected(n, connections) == 0

    print("Quick tests passed")
