# Title: 1135. Connecting Cities With Minimum Cost
# Difficulty: Medium
# Tags: Dijkstra
# Link: https://leetcode.com/problems/connecting-cities-with-minimum-cost/
# Time: O(eloge)  (heap operations dominate; e = len(connections))
# Space: O(n+e)

from typing import List
import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        - Build adjacency list for cities 1..n.
        - Start from city 1; push all outgoing edges into a min-heap.
        - Repeatedly pick the smallest-cost edge that connects a new city.
        - Sum costs until all cities are connected, else return -1.
        """
        if n == 0:
            return 0
        if n == 1:
            return 0

        # Build adjacency list (1-indexed)
        adj = [[] for _ in range(n + 1)]
        for u, v, w in connections:
            adj[u].append((w, v))
            adj[v].append((w, u))

        visited = [False] * (n + 1)
        visited_count = 0
        total_cost = 0

        # Start Prim from node 1
        visited[1] = True
        visited_count += 1
        pq = []
        for w, v in adj[1]:
            heapq.heappush(pq, (w, v))

        # Expand MST
        while pq and visited_count < n:
            w, v = heapq.heappop(pq)
            if visited[v]:
                continue
            visited[v] = True
            visited_count += 1
            total_cost += w
            for nw, nv in adj[v]:
                if not visited[nv]:
                    heapq.heappush(pq, (nw, nv))

        return total_cost if visited_count == n else -1


