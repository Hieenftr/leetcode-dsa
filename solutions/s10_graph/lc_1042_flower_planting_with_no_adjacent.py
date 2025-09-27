# Title: 1042. Flower Planting With No Adjacent
# Difficulty: Medium
# Tags: Graph
# Link: https://leetcode.com/problems/flower-planting-with-no-adjacent/
# Time: O(n+m)
# Space: O(n+m)

from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """
        - Build adjacency list for 1..n (each garden has at most 3 neighbors).
        - For each garden i:
            -Check which colors (1..4) are already used by neighbors.
            - Assign the smallest available color to i.
        """
        # Adjacency list (0-indexed)
        adj = [[] for _ in range(n)]
        for a, b in paths:
            a -= 1; b -= 1
            adj[a].append(b)
            adj[b].append(a)

        res = [0] * n  # flower type for each garden

        for i in range(n):
            used = [False] * 5  # use indices 1..4
            # Mark neighbor colors
            for nei in adj[i]:
                if res[nei] != 0:
                    used[res[nei]] = True
            # Pick the first available color
            for c in range(1, 5):
                if not used[c]:
                    res[i] = c
                    break

        return res
