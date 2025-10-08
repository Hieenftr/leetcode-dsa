# Title: 684. Redundant Connection
# Difficulty: Medium
# Tags: Union Find
# Link: https://leetcode.com/problems/redundant-connection/
# Time: O(n)
# Space: O(n)

from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # union would create a cycle
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Union edges; the first edge that connects two nodes already in the
        same set is the redundant one (forms a cycle).
        """
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        return [] 


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    edges = [[1,2],[1,3],[2,3]]
    assert sol.findRedundantConnection(edges) == [2,3]

    # Example 2
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    assert sol.findRedundantConnection(edges) == [1,4]

    # larger tree with one extra edge
    edges = [[1,2],[2,3],[3,4],[4,5],[2,5]]
    assert sol.findRedundantConnection(edges) == [2,5]

    print("Quick tests passed")
