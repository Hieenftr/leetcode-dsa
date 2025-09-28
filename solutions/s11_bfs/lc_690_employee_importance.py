# Title: 690. Employee Importance
# Difficulty: Medium
# Tags: BFS
# Link: https://leetcode.com/problems/employee-importance/
# Time: O(n)
# Space: O(n)

from typing import List, Dict
from collections import deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        """
        - Build a lookup map {id -> Employee}.
        - Start a queue with the given id.
        - Pop each employee, add their importance, and push subordinates.
        """
        emp_map: Dict[int, Employee] = {}
        for e in employees:
            emp_map[e.id] = e

        total = 0
        queue = deque([id])

        while queue:
            eid = queue.popleft()
            emp = emp_map[eid]
            total += emp.importance
            for sub in emp.subordinates:
                queue.append(sub)

        return total


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [])
    e3 = Employee(3, 3, [])
    employees = [e1, e2, e3]
    assert sol.getImportance(employees, 1) == 11

    # Example 2
    e1 = Employee(1, 2, [5])
    e2 = Employee(5, -3, [])
    employees = [e1, e2]
    assert sol.getImportance(employees, 5) == -3

    # Example 3:
    e1 = Employee(7, 10, [])
    employees = [e1]
    assert sol.getImportance(employees, 7) == 10

    print("Quick tests passed")
