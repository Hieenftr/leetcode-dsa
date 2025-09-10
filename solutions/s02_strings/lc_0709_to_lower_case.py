# Title: 0709. To Lower Case
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/to-lower-case/
# Time: O(n)
# Space: O(n)

class Solution:
    def toLowerCase(self, s: str) -> str:
        """
        Convert a string to lowercase without using str.lower().
        Approach:
        - Iterate through each character.
        - If character is uppercase 'A'..'Z' (ASCII 65–90), convert to lowercase
          by adding 32 to its ASCII code.
        - Otherwise, keep it unchanged.
        - Collect into a list and join at the end.
        """
        out = []
        for ch in s:
            code = ord(ch)
            if 65 <= code <= 90:  # 'A'..'Z'
                out.append(chr(code + 32))
            else:
                out.append(ch)
        return "".join(out)


if __name__ == "__main__":
    sol = Solution()

    assert sol.toLowerCase("Hello") == "hello"
    assert sol.toLowerCase("here") == "here"
    assert sol.toLowerCase("LOVELY") == "lovely"
    # Mixed + non-letters
    assert sol.toLowerCase("AbC123!?") == "abc123!?"
    assert sol.toLowerCase("") == ""

    print("Quick tests passed")
