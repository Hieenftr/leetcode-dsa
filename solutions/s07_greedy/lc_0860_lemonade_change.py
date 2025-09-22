# Title: 0860. Lemonade Change
# Difficulty: Easy
# Tags: Greedy
# Link: https://leetcode.com/problems/lemonade-change/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Greedy: always give change with larger bills first.
        Track count of $5 and $10 bills.
        """
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.lemonadeChange([5,5,5,10,20]) is True
    assert sol.lemonadeChange([5,5,10]) is True
    assert sol.lemonadeChange([10,10]) is False
    assert sol.lemonadeChange([5,5,10,10,20]) is False

    print("Quick tests passed")
