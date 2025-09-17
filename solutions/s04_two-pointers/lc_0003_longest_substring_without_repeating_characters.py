# Title: 0003. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Tags: Two Pointers, Sliding Window, HashMap
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time: O(n)
# Space: O(k)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window + HashMap:
        - Use dict to track last index of each char.
        - Expand right pointer; if char repeats, move left pointer.
        - Keep track of max window length.
        """
        seen = {}   # char:last index
        left = 0
        res = 0

        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                # move left after last occurrence
                left = seen[ch] + 1
            seen[ch] = right
            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("") == 0

    print("Quick tests passed")
