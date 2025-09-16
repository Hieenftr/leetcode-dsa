# Title: 1672. Richest Customer Wealth
# Difficulty: Easy
# Tags: Array
# Link: https://leetcode.com/problems/richest-customer-wealth/
# Time: O(m*n)
# Space: O(1)

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Iterate each customer (row):
        - Compute wealth = sum of accounts
        - Track the maximum wealth seen so far
        """
        wealth_max = 0
        for money in accounts:
            wealth = sum(money)
            if wealth > wealth_max:
                wealth_max = wealth
        return wealth_max


if __name__ == "__main__":
    sol = Solution()

    assert sol.maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert sol.maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17
    assert sol.maximumWealth([[5]]) == 5
    assert sol.maximumWealth([[0,0,0],[0,0,0]]) == 0

    print("Quick tests passed")
