# Title: 997. Find the Town Judge
# Difficulty: Easy
# Tags: Graph
# Link: https://leetcode.com/problems/find-the-town-judge/
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        A town judge is a person who:
        1) Is trusted by everyone else (in-degree = n - 1)
        2) Trusts nobody (out-degree = 0)

        Approach:
        - Maintain score[i] = in_degree(i) - out_degree(i).
        - The judge will have score[j] == n - 1.
        """
        score = [0] * (n + 1)
        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
        return -1
