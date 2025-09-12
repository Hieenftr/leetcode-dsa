# Title: 0925. Long Pressed Name
# Difficulty: Easy
# Tags: String, Two Pointers
# Link: https://leetcode.com/problems/long-pressed-name/
# Time: O(n)
# Space: O(1)

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        Two pointers:
        - i over name, j over typed.
        - If characters match -> advance both.
        - Else typed[j] must match the previous character of name (long press) -> advance j only.
        - If neither holds -> False.
        - At the end, i must have consumed all of name.
        """
        i, j = 0, 0
        n, m = len(name), len(typed)

        while j < m:
            if i < n and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                # long press of previous typed char
                j += 1
            else:
                return False

        return i == n


if __name__ == "__main__":
    s = Solution()

    assert s.isLongPressedName("alex", "aaleex") is True
    assert s.isLongPressedName("alex", "aalexx") is True
    assert s.isLongPressedName("alex", "alx") is False           # missing 'e'
    assert s.isLongPressedName("saeed", "ssaaedd") is False
    assert s.isLongPressedName("leelee", "lleeelee") is True
    assert s.isLongPressedName("laiden", "laiden") is True
    assert s.isLongPressedName("a", "aaaa") is True
    assert s.isLongPressedName("", "aaa") is False               # no base to long-press
    assert s.isLongPressedName("abcd", "aabbccdd") is True
    assert s.isLongPressedName("", "") is True                   

    print("Quick tests passed")
