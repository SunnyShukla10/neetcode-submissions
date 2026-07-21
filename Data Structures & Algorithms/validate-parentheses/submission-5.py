class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for l in s:
            if l in d:
                
                if stack and stack[-1] == d[l]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(l)
                
        
        return len(stack)==0 