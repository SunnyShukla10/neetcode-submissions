class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMax = leftMin = 0

        for l in s:
            if l == "(":
                leftMax += 1
                leftMin += 1
            
            elif l == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            
            if leftMax < 0:
                return False

            if leftMin < 0:
                leftMin = 0
                
        return leftMin == 0 
            