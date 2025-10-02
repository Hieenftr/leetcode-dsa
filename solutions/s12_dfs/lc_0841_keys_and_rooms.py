# Title: 841. Keys and Rooms
# Difficulty: Medium
# Tags: Graph, DFS
# Link: https://leetcode.com/problems/keys-and-rooms/
# Time: O(n+e)   # n = number of rooms, e = number of keys
# Space: O(n)  

from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        - Each room contains keys to other rooms.
        - Start from room 0, collect keys recursively.
        - Keep track of visited rooms.
        - If number of visited rooms == total rooms, return True.
        """
        n = len(rooms)
        visited = [False] * n

        def dfs(room: int):
            visited[room] = True
            for key in rooms[room]:
                if not visited[key]:
                    dfs(key)

        dfs(0)
        return all(visited)


if __name__ == "__main__":
    sol = Solution()

    rooms = [[1],[2],[3],[]]
    assert sol.canVisitAllRooms(rooms) == True

    rooms = [[1,3],[3,0,1],[2],[0]]
    assert sol.canVisitAllRooms(rooms) == False

    rooms = [[]]
    assert sol.canVisitAllRooms(rooms) == True

    rooms = [[1],[],[3],[]]
    assert sol.canVisitAllRooms(rooms) == False

    print("Quick tests passed")
