# Title: 0013. Roman to Integer
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/roman-to-integer/
# Time: O(n)
# Space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            if i + 1 < n and values[s[i]] < values[s[i+1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total


if __name__ == "__main__":
    sol = Solution()

    assert sol.romanToInt("III") == 3
    assert sol.romanToInt("IV") == 4
    assert sol.romanToInt("IX") == 9
    assert sol.romanToInt("LVIII") == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    assert sol.romanToInt("XL") == 40
    assert sol.romanToInt("CD") == 400
    assert sol.romanToInt("CM") == 900

    print("Quick tests passed")
