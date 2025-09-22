# Title: 0455. Assign Cookies
# Difficulty: Easy
# Tags: Greedy
# Link: https://leetcode.com/problems/assign-cookies/
# Time: O(nlogn)
# Space: O(1)

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Greedy: sort g and s, give the smallest cookie that can satisfy a child.
        """
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i


if __name__ == "__main__":
    sol = Solution()

    assert sol.findContentChildren([1,2,3], [1,1]) == 1
    assert sol.findContentChildren([1,2], [1,2,3]) == 2
    assert sol.findContentChildren([10,9,8,7], [5,6,7,8]) == 2

    print("Quick tests passed")
