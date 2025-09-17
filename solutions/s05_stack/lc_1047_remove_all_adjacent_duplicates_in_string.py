# Title: 1047. Remove All Adjacent Duplicates In String
# Difficulty: Easy
# Tags: Stack
# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Time: O(n)
# Space: O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        - Traverse chars, push into stack.
        - If top of stack == current char, pop (remove duplicate pair).
        - Else push current char.
        """
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)


if __name__ == "__main__":
    sol = Solution()

    assert sol.removeDuplicates("abbaca") == "ca"
    assert sol.removeDuplicates("azxxzy") == "ay"
    assert sol.removeDuplicates("a") == "a"

    print("Quick tests passed")
