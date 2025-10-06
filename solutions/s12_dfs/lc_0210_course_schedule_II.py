# Title: 210. Course Schedule II
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/course-schedule-ii/
# Time: O(v+e)
# Space: O(v+e)

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        - Build adjacency list where course -> prerequisites.
        - Use DFS to detect cycles and collect topological order.
        - States:
            0 = unvisited, 1 = visiting, 2 = visited.
        - Append nodes postorder (when fully processed).
        - If cycle detected → return [].
        """
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        order = []
        has_cycle = False

        def dfs(node: int):
            nonlocal has_cycle
            if has_cycle:
                return
            if state[node] == 1:  # cycle detected
                has_cycle = True
                return
            if state[node] == 2:
                return

            state[node] = 1
            for nei in graph[node]:
                dfs(nei)
            state[node] = 2
            order.append(node)

        for i in range(numCourses):
            if state[i] == 0:
                dfs(i)
                if has_cycle:
                    return []

        return order[::-1]


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    numCourses = 2
    prerequisites = [[1,0]]
    assert sol.findOrder(numCourses, prerequisites) == [0,1]

    # Example 2
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    res = sol.findOrder(numCourses, prerequisites)
    assert res in ([0,2,1,3], [0,1,2,3])

    # Example 3 (cycle)
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    assert sol.findOrder(numCourses, prerequisites) == []


    print("Quick tests passed")
