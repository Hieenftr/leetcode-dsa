# Title: 0121. Best Time to Buy and Sell Stock
# Difficulty: Easy
# Tags: Greedy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Track the minimum price so far and compute
        max profit if sold today.
        """
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            else:
                max_profit = max(max_profit, p - min_price)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7,1,5,3,6,4]) == 5   # buy=1, sell=6
    assert sol.maxProfit([7,6,4,3,1]) == 0    # no profit
    assert sol.maxProfit([2,4,1]) == 2
    assert sol.maxProfit([1,2]) == 1

    print("Quick tests passed")
