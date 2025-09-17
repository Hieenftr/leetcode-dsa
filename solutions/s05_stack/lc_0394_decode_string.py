# Title: 0394. Decode String
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/decode-string/
# Time: O(n)
# Space: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Approach:
        - Traverse characters.
        - If digit: build number.
        - If '[': push (cur_str, num) to stack, reset.
        - If ']': pop (prev_str, num), cur_str = prev_str + num*cur_str.
        - Else: append character to cur_str.
        """
        stack = []
        cur_str = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_str, num))
                cur_str = ""
                num = 0
            elif ch == "]":
                prev_str, k = stack.pop()
                cur_str = prev_str + k * cur_str
            else:
                cur_str += ch

        return cur_str


if __name__ == "__main__":
    sol = Solution()

    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"

    print("Quick tests passed")
