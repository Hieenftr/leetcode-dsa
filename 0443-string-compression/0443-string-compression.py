class Solution:
    def compress(self, chars: List[str]) -> int:
        
        read = write = 0
        n = len(chars)

        while read < n:
            letter = chars[read]
            start = read

            while read < n and chars[read] == letter:
                read += 1
            count = read - start

            chars[write] = letter
            write += 1

            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        
        return write