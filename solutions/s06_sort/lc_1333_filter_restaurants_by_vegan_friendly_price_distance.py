# Title: 1333. Filter Restaurants by Vegan-Friendly, Price and Distance
# Difficulty: Medium
# Tags: Sort
# Link: https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# Time: O(nlogn)
# Space: O(n)

from typing import List

class Solution:
    def filterRestaurants(
        self,
        restaurants: List[List[int]],
        veganFriendly: int,
        maxPrice: int,
        maxDistance: int
    ) -> List[int]:
        """
        Filter by conditions then sort:
        - Only include veganFriendly ones if required.
        - Must satisfy price <= maxPrice and distance <= maxDistance.
        - Sort by rating desc, then id desc.
        """
        filtered = []
        for r in restaurants:
            rid, rating, vegan, price, dist = r
            if veganFriendly and vegan == 0:
                continue
            if price > maxPrice or dist > maxDistance:
                continue
            filtered.append(r)

        # sort by rating desc, then id desc
        filtered.sort(key=lambda x: (-x[1], -x[0]))

        return [r[0] for r in filtered]


if __name__ == "__main__":
    sol = Solution()

    restaurants = [
        [1,4,1,40,10],
        [2,8,0,50,5],
        [3,8,1,30,4],
        [4,10,0,10,3],
        [5,1,1,15,1]
    ]
    assert sol.filterRestaurants(restaurants, 1, 50, 10) == [3,1,5]
    assert sol.filterRestaurants(restaurants, 0, 50, 10) == [4,3,2,1,5]
    assert sol.filterRestaurants(restaurants, 0, 30, 3) == [4,5]

    print("Quick tests passed")
