# Title: 1029. Two City Scheduling
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/two-city-scheduling/
# Time: O(nlogn)
# Space: O(1)

from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Greedy:
        - Assume all go to A.
        - Sort people by delta = bCost - aCost.
        - Pick n smallest deltas to go to B.
        """
        n = len(costs) // 2
        total = sum(a for a, b in costs)
        deltas = sorted(b - a for a, b in costs)
        total += sum(deltas[:n])
        return total


if __name__ == "__main__":
    sol = Solution()

    assert sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110
    assert sol.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859
    assert sol.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]) == 3086

    print("Quick tests passed")
