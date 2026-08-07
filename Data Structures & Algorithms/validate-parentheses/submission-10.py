class Solution:
    def isValid(self, s: str) -> bool:
        d = { 
            ")":"(",
            "]":"[",
            "}":"{"
        } 

        stack = []

        for char in s:
            if char in d and stack:
                val = stack.pop()
                if val != d[char]:
                    return False
            else:
                stack.append(char)
        print(stack)
        return len(stack) == 0