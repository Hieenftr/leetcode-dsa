# Title: 0406. Queue Reconstruction by Height
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/queue-reconstruction-by-height/
# Time: O(n^2)
# Space: O(n)

from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Greedy:
        - Sort by height desc, k asc.
        - Insert each person into result at index = k.
        """
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]) == [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    assert sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]) == [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

    print("Quick tests passed")
