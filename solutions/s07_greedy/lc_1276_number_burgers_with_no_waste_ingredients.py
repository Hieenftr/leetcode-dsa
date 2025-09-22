# Title: 1276. Number of Burgers with No Waste of Ingredients
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
# Time: O(1)
# Space: O(1)

from typing import List

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # tomatoes must be even
        if tomatoSlices % 2 != 0:
            return []
        x = tomatoSlices // 2 - cheeseSlices            # jumbo
        y = 2 * cheeseSlices - tomatoSlices // 2        # small
        if x < 0 or y < 0:
            return []
        return [x, y]


if __name__ == "__main__":
    sol = Solution()

    assert sol.numOfBurgers(16, 7) == [1, 6]
    assert sol.numOfBurgers(17, 4) == []
    assert sol.numOfBurgers(4, 17) == []
    assert sol.numOfBurgers(0, 0) == [0, 0]
    assert sol.numOfBurgers(2, 1) == [0, 1]

    print("Quick tests passed")
