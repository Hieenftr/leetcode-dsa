# Title: 1119. Remove Vowels from a String
# Difficulty: Easy
# Tags: String, Two Pointers
# Link: https://leetcode.com/problems/remove-vowels-from-a-string/
# Time: O(n)
# Space: O(n)

class Solution:
    def removeVowels(self, s: str) -> str:
        """
        Remove lowercase vowels from the string.
        Use a hash set for O(1) membership checks and build the result via list join.
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        out = []
        for ch in s:
            if ch not in vowels:
                out.append(ch)
        return "".join(out)


if __name__ == "__main__":
    sol = Solution()

    assert sol.removeVowels("leetcodeisacommunityforcoders") == "ltcdscmmntyfrcdrs"
    assert sol.removeVowels("aeiou") == ""
    assert sol.removeVowels("aAeiIOuU") == ""
    assert sol.removeVowels("bcdfg") == "bcdfg"
    assert sol.removeVowels("hello") == "hll"
    assert sol.removeVowels("programming") == "prgrmmng"

    # Edge cases
    assert sol.removeVowels("") == ""
    assert sol.removeVowels("a") == ""
    assert sol.removeVowels("b") == "b"

    print("Quick tests passed")