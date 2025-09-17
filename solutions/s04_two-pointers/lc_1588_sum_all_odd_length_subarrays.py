# Title: 1588. Sum of All Odd Length Subarrays (Two Pointers)
# Difficulty: Easy
# Tags: Two Pointers, Sliding Window
# Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
# Time: O(n^2)
# Space: O(1)

from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        """
        Sliding window over all odd lengths:
        - For each odd L in [1..n]: compute sum of every window of length L.
        - Maintain a rolling window sum while moving two pointers (left, right).
        """
        n = len(arr)
        total = 0

        # iterate odd window lengths
        for L in range(1, n + 1, 2):
            # init window [0..L-1]
            window_sum = sum(arr[0:L])
            total += window_sum

            left, right = 0, L - 1
            # slide window to the right
            while right + 1 < n:
                left += 1
                right += 1
                window_sum += arr[right] - arr[left - 1]
                total += window_sum

        return total


if __name__ == "__main__":
    sol = Solution()

    assert sol.sumOddLengthSubarrays([1,4,2,5,3]) == 58
    assert sol.sumOddLengthSubarrays([1,2]) == 3
    assert sol.sumOddLengthSubarrays([10,11,12]) == 66

    print("Quick tests passed")
