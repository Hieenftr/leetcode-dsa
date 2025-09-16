# Title: 0088. Merge Sorted Array
# Difficulty: Easy
# Tags: Two Pointers
# Link: https://leetcode.com/problems/merge-sorted-array/
# Time: O(m+n)
# Space: O(1)


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Two pointers from the end:
        - p1: last valid element in nums1
        - p2: last element in nums2
        - p:  last index in nums1
        Compare from the back and fill nums1 in-place.
        """
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,3,0,0,0]; m=3
    nums2 = [2,5,6]; n=3
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

    nums1 = [1]; m=1
    nums2 = []; n=0
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [0]; m=0
    nums2 = [1]; n=1
    sol.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    print("Quick tests passed")