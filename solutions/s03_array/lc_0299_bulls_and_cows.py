# Title: 0299. Bulls and Cows (Array Version)
# Difficulty: Medium
# Tags: String, Array
# Link: https://leetcode.com/problems/bulls-and-cows/
# Time: O(n)
# Space: O(1)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        """
        - Use freq[10] to balance counts for secret and guess mismatches.
        - If a digit from secret was seen more times in guess (or vice versa),
          we count a cow when balance crosses zero.
        """
        bulls = cows = 0
        freq = [0] * 10

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_digit, g_digit = int(s), int(g)

                if freq[s_digit] < 0:
                    cows += 1
                if freq[g_digit] > 0:
                    cows += 1

                freq[s_digit] += 1
                freq[g_digit] -= 1

        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    sol = Solution()

    assert sol.getHint("1807", "7810") == "1A3B"
    assert sol.getHint("1123", "0111") == "1A1B"
    assert sol.getHint("1", "0") == "0A0B"
    assert sol.getHint("1", "1") == "1A0B"
    assert sol.getHint("1122", "2211") == "0A4B"
    
    print("Quick tests passed")
