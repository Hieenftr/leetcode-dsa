# Title: 323. Number of Connected Components in an Undirected Graph
# Difficulty: Medium
# Tags: Union-Find
# Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Time: O(e * α(v))
# Space: O(v)

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n  # number of connected components

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return
        if self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB
        elif self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA
        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1
        self.count -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        - Start with n isolated components.
        - Union nodes for each edge.
        - Result = number of unique components left.
        """
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.count


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    assert sol.countComponents(n, edges) == 2

    # Example 2
    n = 5
    edges = [[0,1],[1,2],[2,3],[3,4]]
    assert sol.countComponents(n, edges) == 1

    # Example 3: no edges
    n = 4
    edges = []
    assert sol.countComponents(n, edges) == 4

    # Example 4: isolated node
    n = 3
    edges = [[0,1]]
    assert sol.countComponents(n, edges) == 2

    print("Quick tests passed")
