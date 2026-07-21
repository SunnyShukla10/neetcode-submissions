class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30,31,30] --> [1,0,0]
        res = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            if stack:
                while stack and val > stack[-1][1]:
                    idx, v = stack.pop()
                    print("i: ", i)
                    print(idx, " ", v)
                    res[idx] = i - idx
            stack.append((i,val))
        
        return res

#       stack = [(1, 38), (3, 36)]
#       outpu = [  1, , 1, ,1 ,   ]