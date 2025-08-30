class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for letter in s:
            if not stack:               
                stack.append(letter)
            else:
                if stack[-1] == letter:  
                    stack.pop()
                else:                    
                    stack.append(letter)

        return "".join(stack)