# Title: 1518. Water Bottles
# Difficulty: Easy
# Tags: Greedy
# Link: https://leetcode.com/problems/water-bottles/
# Time: O(numBottles)
# Space: O(1)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        Drink all full bottles. After each round:
        - Exchange empty bottles for new full ones.
        - Keep track of total drunk.
        """
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            new_full = empty // numExchange
            total += new_full
            empty = empty % numExchange + new_full

        return total


if __name__ == "__main__":
    sol = Solution()

    assert sol.numWaterBottles(9, 3) == 13
    assert sol.numWaterBottles(15, 4) == 19
    assert sol.numWaterBottles(5, 5) == 6
    assert sol.numWaterBottles(2, 3) == 2

    print("Quick tests passed")
