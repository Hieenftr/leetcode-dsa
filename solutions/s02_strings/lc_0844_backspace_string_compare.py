# Title: 0844. Backspace String Compare
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/backspace-string-compare/
# Time: O(n)
# Space: O(n)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        Simulate typing with backspaces using stacks.
        """
        def build(string: str) -> str:
            stack = []
            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return "".join(stack)

        return build(s) == build(t)


if __name__ == "__main__":
    sol = Solution()

    assert sol.backspaceCompare("ab#c", "ad#c") is True   # "ac"
    assert sol.backspaceCompare("ab##", "c#d#") is True   # ""
    assert sol.backspaceCompare("a#c", "b") is False
    assert sol.backspaceCompare("", "") is True
    assert sol.backspaceCompare("###", "") is True
    assert sol.backspaceCompare("bxj##tw", "bxo#j##tw") is True
    assert sol.backspaceCompare("xy#z", "xzz#") is True   # "xz"

    print("Quick tests passed")
