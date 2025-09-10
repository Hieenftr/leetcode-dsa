# Title: 1247. Minimum Swap to Make Strings Equal
# Difficulty: Medium
# Tags: String
# Link: https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
# Time: O(n)
# Space: O(1)

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        """
        Count mismatch types:
        - xy: positions where s1[i]='x', s2[i]='y'
        - yx: positions where s1[i]='y', s2[i]='x'
        Rules:
        - If (xy + yx) is odd -> impossible -> -1
        - Otherwise, swaps = xy//2 + yx//2 + 2*(xy%2)
          (two 'xy' form 1 swap, two 'yx' form 1 swap,
           one 'xy' + one 'yx' (odd-odd) costs 2 swaps)
        """
        if len(s1) != len(s2):
            return -1

        xy = yx = 0
        for a, b in zip(s1, s2):
            if a == b:
                continue
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
            else:
                # outside 'x'/'y' alphabet -> not in original constraints
                return -1

        total = xy + yx
        if total % 2 == 1:
            return -1

        return xy // 2 + yx // 2 + 2 * (xy % 2)


if __name__ == "__main__":
    s = Solution()

    assert s.minimumSwap("xx", "yy") == 1
    assert s.minimumSwap("xy", "yx") == 2
    assert s.minimumSwap("xx", "xy") == -1
    assert s.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx") == 4
    assert s.minimumSwap("xyxy", "yxyx") == 2
    assert s.minimumSwap("xxxx", "yyyy") == 2
    assert s.minimumSwap("", "") == 0
    assert s.minimumSwap("x", "x") == 0
    assert s.minimumSwap("x", "y") == -1

    print("Quick tests passec")
