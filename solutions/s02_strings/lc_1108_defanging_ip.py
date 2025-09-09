# Title: 1108. Defanging an IP Address
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/defanging-an-ip-address/
# Time: O(n)
# Space: O(n)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Replace every '.' with '[.]' in the given IP address string.
        """
        return address.replace(".", "[.]")


if __name__ == "__main__":
    sol = Solution()

    assert sol.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert sol.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
    assert sol.defangIPaddr("0.0.0.0") == "0[.]0[.]0[.]0"
    assert sol.defangIPaddr("127.0.0.1") == "127[.]0[.]0[.]1"

    print("Quick tests passed")