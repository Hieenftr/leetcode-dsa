# Title: 1441. Build an Array With Stack Operations
# Difficulty: Easy
# Tags: Stack
# Link: https://leetcode.com/problems/build-an-array-with-stack-operations/
# Time: O(max(target))
# Space: O(len(target))

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        """
        Simulation with stack ops:
        - Traverse numbers from 1..n.
        - If num matches target[j]: Push and move j.
        - Else: Push + Pop (skip this num).
        - Stop when j == len(target).
        """
        res = []
        j = 0  # pointer in target

        for num in range(1, n + 1):
            if j == len(target):
                break
            if num == target[j]:
                res.append("Push")
                j += 1
            else:
                res.append("Push")
                res.append("Pop")

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.buildArray([1,3], 3) == ["Push","Push","Pop","Push"]
    assert sol.buildArray([1,2,3], 3) == ["Push","Push","Push"]
    assert sol.buildArray([1,2], 4) == ["Push","Push"]
    print("Quick tests passed")
