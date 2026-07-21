class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # 30 38 30 40
        # stack: [(30,0), (38,1)] <- front
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _ , idx = stack.pop()
                res[idx] = i - idx
            stack.append((t,i))
        
        return res
            