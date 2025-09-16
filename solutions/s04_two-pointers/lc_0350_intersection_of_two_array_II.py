# Title: 0350. Intersection of Two Arrays II
# Difficulty: Easy
# Tags: Two Pointers
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Time: O(nlogn + mlogm)
# Space: O(1)

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        - Sort both arrays.
        - Use two pointers i, j:
          * If nums1[i] == nums2[j]: add to result, move both.
          * If nums1[i] < nums2[j]: move i.
          * Else: move j.
        - Continue until one pointer reaches the end.
        """
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res


if __name__ == "__main__":
    sol = Solution()

    assert sol.intersect([1,2,2,1], [2,2]) == [2,2]
    assert sol.intersect([4,9,5], [9,4,9,8,4]) in [[4,9],[9,4]]
    assert sol.intersect([], [1,2]) == []
    assert sol.intersect([1,2,3], [4,5,6]) == []
    
    print("Quick tests passed")
