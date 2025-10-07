# Title: 743. Network Delay Time
# Difficulty: Medium
# Tags: Dijkstra
# Link: https://leetcode.com/problems/network-delay-time/
# Time: O((e+v) log v)
# Space: O(e+v)

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra from source k:
        - Build adjacency list: u -> [(v, w), ...]
        - Use min-heap (dist, node). Pop smallest, relax edges.
        - Answer = max distance among all nodes if all reachable; else -1.
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        INF = 10**15
        dist = [INF] * (n + 1)
        dist[k] = 0

        pq = [(0, k)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        ans = max(dist[1:])  # ignore index 0
        return -1 if ans == INF else ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n, k = 4, 2
    assert sol.networkDelayTime(times, n, k) == 2

    # Example 2: unreachable node
    times = [[1,2,1]]
    n, k = 2, 1
    assert sol.networkDelayTime(times, n, k) == 1
    n, k = 2, 2
    assert sol.networkDelayTime(times, n, k) == -1

    # Multiple edges, pick smaller weight
    times = [[1,2,5],[1,2,1],[2,3,2],[1,3,10]]
    n, k = 3, 1
    assert sol.networkDelayTime(times, n, k) == 3  # 1->2 (1), 2->3 (2)

    # Single node
    times = []
    n, k = 1, 1
    assert sol.networkDelayTime(times, n, k) == 0

    print("Quick tests passed")
