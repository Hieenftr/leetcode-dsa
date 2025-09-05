# Title: 394. Decode String
# Difficulty: Medium
# Tags: Stack, String
# Link: https://leetcode.com/problems/decode-string/
# Time: O(n)
# Space: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Approach:
        - Use a stack to keep (prev_str, repeat_count).
        - Iterate characters:
          * digit -> build current number
          * '['   -> push (current_string, current_number), reset both
          * ']'   -> pop and expand: prev + cur*repeat
          * char  -> append to current_string

        Why it works:
        - Brackets form natural nested segments; stack preserves context.
        """
        stack = []
        cur_str = []
        cur_num = 0

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                stack.append(("".join(cur_str), cur_num))
                cur_str, cur_num = [], 0
            elif ch == ']':
                prev_str, k = stack.pop()
                cur_str = [prev_str + "".join(cur_str) * k]
            else:
                cur_str.append(ch)

        return "".join(cur_str)
