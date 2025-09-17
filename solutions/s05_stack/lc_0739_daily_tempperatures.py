# Title: 0739. Daily Temperatures
# Difficulty: Medium
# Tags: Monotonic Stack
# Link: https://leetcode.com/problems/daily-temperatures/
# Time: O(n)
# Space: O(n)

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack:
        - Keep stack of indices with decreasing temps.
        - For each day i:
            - While current temp > temp[stack[-1]], pop j and set ans[j] = i - j.
            - Push i to stack.
        """
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans


if __name__ == "__main__":
    sol = Solution()

    assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert sol.dailyTemperatures([30,60,90]) == [1,1,0]
    
    print("Quick tests passed")
