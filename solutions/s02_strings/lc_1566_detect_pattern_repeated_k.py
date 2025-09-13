# Title: 1566. Detect Pattern of Length M Repeated K or More Times
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Count consecutive matches with offset m.
        If we see (k-1)*m consecutive matches arr[i] == arr[i-m],
        then there exists k consecutive blocks of length m that are equal.
        """
        n = len(arr)
        if m * k > n:
            return False

        cnt = 0
        for i in range(m, n):
            if arr[i] == arr[i - m]:
                cnt += 1
                if cnt >= (k - 1) * m:
                    return True
            else:
                cnt = 0
        return False


if __name__ == "__main__":
    s = Solution()

    assert s.containsPattern([1,2,4,4,4,4], 1, 3) is True
    assert s.containsPattern([1,2,1,2,1,1,1,3], 2, 2) is True
    assert s.containsPattern([1,2,1,2,1,3], 2, 3) is False
    assert s.containsPattern([2,2], 2, 2) is False
    assert s.containsPattern([3,3,3,3], 1, 4) is True

    print("Quick tests passed")
