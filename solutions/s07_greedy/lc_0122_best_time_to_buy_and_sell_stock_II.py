# Title: 0122. Best Time to Buy and Sell Stock II
# Difficulty: Medium
# Tags: Greedy
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Sum all positive day-to-day increases.
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == "__main__":
    sol = Solution()
    
    assert sol.maxProfit([7,1,5,3,6,4]) == 7   
    assert sol.maxProfit([1,2,3,4,5]) == 4    
    assert sol.maxProfit([7,6,4,3,1]) == 0     # no rises
    assert sol.maxProfit([2,1,2,0,1]) == 2

    print("Quick tests passed ")
