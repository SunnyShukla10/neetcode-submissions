class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                # check size diff
                diff = a + stack[-1]
                if diff > 0:
                    a = 0 # don't want to append 
                elif diff < 0:
                    stack.pop()
                else:
                    stack.pop()
                    a = 0 # don't want to append 
            if a:
                stack.append(a)
        return stack