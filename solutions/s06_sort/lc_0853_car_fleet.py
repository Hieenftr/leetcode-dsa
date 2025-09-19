# Title: 0853. Car Fleet
# Difficulty: Medium
# Tags: Sort
# Link: https://leetcode.com/problems/car-fleet/
# Time: O(nlogn)
# Space: O(n)

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Sort cars by starting position descending.
        Track arrival times to destination.
        Count a new fleet when a car's time is strictly greater
        than the max_time of fleets ahead.
        """
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        max_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets


if __name__ == "__main__":
    sol = Solution()

    assert sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0,2,4], [4,2,1]) == 1
    assert sol.carFleet(10, [6,8], [3,2]) == 2
    
    print("Quick tests passed")
