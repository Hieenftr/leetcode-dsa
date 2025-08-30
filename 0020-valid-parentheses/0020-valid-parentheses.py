class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:    
            return False

        open_set = {'(', '[', '{'}
        map_match = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in open_set:   
                stack.append(ch)
            else:               
                if stack and stack[-1] == map_match[ch]:
                    stack.pop()  
                else:
                    return False 

        return not stack         