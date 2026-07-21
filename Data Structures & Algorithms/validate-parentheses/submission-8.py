class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []
        
        for p in s:    
            # we found a closing parenthesis
            if p in d:
                if stack and stack[-1] == d[p]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0