# Title: 1129. Shortest Path with Alternating Colors
# Difficulty: Medium
# Tags: BFS
# Link: https://leetcode.com/problems/shortest-path-with-alternating-colors/
# Time: O(n+r+b)   # r, b = number of red/blue edges
# Space: O(n+r+b)

from typing import List
from collections import deque

RED, BLUE = 0, 1

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """
        - BFS on (node, last_color). From last_color=c we can only take edges of color 1-c.
        - Start from node 0 with both colors allowed (push (0,RED) and (0,BLUE) at distance 0).
        - Keep dist[node][color] = shortest distance ending at node with last edge = color.
        - Result for node i is min(dist[i][RED], dist[i][BLUE]) (or -1 if both inf).
        """
        # Build adjacency lists by color
        adj = [ [[] for _ in range(n)] , [[] for _ in range(n)] ]  # adj[color][u] -> list of v
        for u, v in redEdges:
            adj[RED][u].append(v)
        for u, v in blueEdges:
            adj[BLUE][u].append(v)

        INF = 10**9
        dist = [[INF]*n for _ in range(2)]
        dist[RED][0] = 0
        dist[BLUE][0] = 0

        q = deque()
        q.append((0, RED))
        q.append((0, BLUE))

        while q:
            u, c = q.popleft()
            nxt_color = 1 - c
            for v in adj[nxt_color][u]:
                if dist[nxt_color][v] == INF:
                    dist[nxt_color][v] = dist[c][u] + 1
                    q.append((v, nxt_color))

        ans = []
        for i in range(n):
            d = min(dist[RED][i], dist[BLUE][i])
            ans.append(-1 if d == INF else d)
        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    n = 3
    redEdges = [[0,1],[1,2]]
    blueEdges = []
    assert sol.shortestAlternatingPaths(n, redEdges, blueEdges) == [0,1,-1]

    # Example 2
    n = 3
    redEdges = [[0,1]]
    blueEdges = [[2,1]]
    assert sol.shortestAlternatingPaths(n, redEdges, blueEdges) == [0,1,-1]

    print("Quick tests passed")
