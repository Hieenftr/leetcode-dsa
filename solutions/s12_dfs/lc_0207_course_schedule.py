# Title: 207. Course Schedule
# Difficulty: Medium
# Tags: DFS
# Link: https://leetcode.com/problems/course-schedule/
# Time: O(v+e)
# Space: O(v+e)

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        - Build adjacency list graph of prerequisites.
        - For each course, run DFS to check if there's a cycle.
        - States:
            0 = unvisited
            1 = visiting (on current path)
            2 = visited (safe)
        - If any DFS finds a cycle, return False.
        """
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)

        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done

        def dfs(node: int) -> bool:
            if state[node] == 1:  # cycle
                return False
            if state[node] == 2:  # already checked
                return True

            state[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()

    # Example 1: possible
    numCourses = 2
    prerequisites = [[1,0]]
    assert sol.canFinish(numCourses, prerequisites) == True

    # Example 2: cycle
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    assert sol.canFinish(numCourses, prerequisites) == False

    # Example 3: larger, no cycle
    numCourses = 4
    prerequisites = [[1,0],[2,1],[3,2]]
    assert sol.canFinish(numCourses, prerequisites) == True

    # Example 4: larger, cycle exists
    numCourses = 4
    prerequisites = [[1,0],[2,1],[3,2],[1,3]]
    assert sol.canFinish(numCourses, prerequisites) == False

    print("Quick tests passed")
