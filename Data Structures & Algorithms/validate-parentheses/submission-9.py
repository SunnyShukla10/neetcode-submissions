class Solution:
    def isValid(self, s: str) -> bool:
        # valid parenthese is you have a ( ) not a ) (
        # ([]) [()] 

        stack = []

        d = {")" : "(", "]":"[", "}":"{" } 

        for i in range(len(s)):

            if stack and s[i] in d:
                val = stack.pop()
                if val != d[s[i]]:
                    return False
                continue

            stack.append(s[i])
        
        return True if not stack else False    