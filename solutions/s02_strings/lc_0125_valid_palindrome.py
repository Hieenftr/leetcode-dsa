# Title: 0125. Valid Palindrome
# Difficulty: Easy
# Tags: String
# Link: https://leetcode.com/problems/valid-palindrome/
# Time: O(n)
# Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointers approach:
        - Move left and right towards each other.
        - Skip non-alphanumeric characters.
        - Compare lowercase characters.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # Skip non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("Madam") is True
    assert sol.isPalindrome("12321") is True
    assert sol.isPalindrome("123ab321") is False
    assert sol.isPalindrome("No 'x' in Nixon") is True

    print("Quick tests passed")
