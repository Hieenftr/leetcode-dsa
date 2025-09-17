# Title: 1249. Minimum Remove to Make Valid Parentheses
# Difficulty: Medium
# Tags: Stack
# Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# Time: O(n)
# Space: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Stack + Set:
        - Track unmatched '(' in stack.
        - Track unmatched ')' in remove set.
        - Remove all invalid indices.
        """
        stack = []
        remove = set()

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # add remaining '(' indices in stack to remove
        remove.update(stack)

        # build result
        res = []
        for i, ch in enumerate(s):
            if i not in remove:
                res.append(ch)

        return "".join(res)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert sol.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert sol.minRemoveToMakeValid("))((") == ""
    assert sol.minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"
    
    print("Quick tests passed")
