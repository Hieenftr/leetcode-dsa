# Title: 1248. Count Number of Nice Subarrays
# Difficulty: Medium
# Tags: Array
# Link: https://leetcode.com/problems/count-number-of-nice-subarrays/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Approach:
        - Use sliding window to count subarrays with at most K odd numbers.
        - Then result = atMost(k) - atMost(k-1).
        """

        def atMost(K: int) -> int:
            count = 0
            left = 0
            odds = 0
            for right, num in enumerate(nums):
                if num % 2 == 1:
                    odds += 1
                while odds > K:
                    if nums[left] % 2 == 1:
                        odds -= 1
                    left += 1
                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)


if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfSubarrays([1,1,2,1,1], 3) == 2
    assert sol.numberOfSubarrays([2,4,6], 1) == 0
    assert sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2) == 16
    assert sol.numberOfSubarrays([1], 1) == 1
    assert sol.numberOfSubarrays([1], 2) == 0
    assert sol.numberOfSubarrays([1,2,3,4,5], 2) == 4

    print("Quick tests passed")
