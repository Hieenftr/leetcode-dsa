# Title: 0443. String Compression
# Difficulty: Medium
# Tags: Two Pointers
# Link: https://leetcode.com/problems/string-compression/
# Time: O(n)
# Space: O(1)

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Two pointers in-place:
        - Use 'read' to scan chars.
        - Use 'write' to overwrite with compressed result.
        - For each group of identical chars:
            * Write the char.
            * If count > 1, write digits of count.
        - Return new length.
        """
        read = write = 0
        n = len(chars)

        while read < n:
            letter = chars[read]
            start = read

            # count consecutive chars
            while read < n and chars[read] == letter:
                read += 1
            count = read - start

            # write the char
            chars[write] = letter
            write += 1

            # write count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


if __name__ == "__main__":
    sol = Solution()
    
    arr1 = ["a","a","b","b","c","c","c"]
    length1 = sol.compress(arr1)
    assert arr1[:length1] == ["a","2","b","2","c","3"]

    arr2 = ["a"]
    length2 = sol.compress(arr2)
    assert arr2[:length2] == ["a"]

    arr3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    length3 = sol.compress(arr3)
    assert arr3[:length3] == ["a","b","1","2"]

    print("Quick tests passed")
