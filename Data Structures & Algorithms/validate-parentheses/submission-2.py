class Solution:
    def isValid(self, s: str) -> bool:
        d = {")":"(", 
             "]":"[",
             "}":"{"}

        stack = []
        if s[0] in d:
            return False
        
        for l in s:
            if l not in d:
                stack.append(l)
            else:
                if stack and stack[-1] == d[l]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0