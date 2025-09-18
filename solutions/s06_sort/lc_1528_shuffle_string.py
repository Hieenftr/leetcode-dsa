# Title: 1528. Shuffle String (Sort version)
# Difficulty: Easy
# Tags: Sort
# Link: https://leetcode.com/problems/shuffle-string/
# Time: O(nlogn)
# Space: O(n)

from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        """
        Sort approach:
        - Pair each char with its target index.
        - Sort pairs by index.
        - Concatenate chars in order.
        """
        new_str = ''
        for item in sorted(list(zip(indices, s))):
            new_str += item[1]

        return new_str



if __name__ == "__main__":
    sol = Solution()

    assert sol.restoreString("codeleet", [4,5,6,7,0,2,1,3]) == "leetcode"
    assert sol.restoreString("abc", [0,1,2]) == "abc"
    assert sol.restoreString("aiohn", [3,1,4,2,0]) == "nihao"
    assert sol.restoreString("aaiougrt", [4,0,2,6,7,3,1,5]) == "arigatou"
    assert sol.restoreString("art", [1,0,2]) == "rat"

    print("Quick tests passed")

