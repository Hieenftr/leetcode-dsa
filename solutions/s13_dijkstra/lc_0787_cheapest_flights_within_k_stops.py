# Title: 787. Cheapest Flights Within K Stops
# Difficulty: Medium
# Tags: Dijkstra
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Time: 
# Space:

from typing import List
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        - Each state tracks current city and number of edges used so far (stops).
        - We can use at most k stops => at most k+1 edges.
        - dist[city][s] = min cost to reach 'city' using exactly s edges.
        - Use a min-heap ordered by cost.
        """
        # Build adjacency list: u -> [(v, w)]
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))

        INF = 10**15
        # dist[city][s] = min cost with exactly s edges (0..k+1)
        dist = [[INF] * (k + 2) for _ in range(n)]
        dist[src][0] = 0

        # Heap entries: (cost, city, used_edges)
        pq = [(0, src, 0)]
        while pq:
            cost, u, used = heapq.heappop(pq)
            # If we popped a worse state, skip
            if cost > dist[u][used]:
                continue
            # Reached destination with minimal cost (heap-ordered)
            if u == dst:
                return cost
            # Expand if we can still take another edge
            if used < k + 1:
                for v, w in adj[u]:
                    nc = cost + w
                    ne = used + 1
                    if nc < dist[v][ne]:
                        dist[v][ne] = nc
                        heapq.heappush(pq, (nc, v, ne))

        # No path found within k stops
        return -1

