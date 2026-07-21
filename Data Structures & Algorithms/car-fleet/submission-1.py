class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create a pair of position, speed per car
        cars = [[p,s] for p,s in zip(position,speed)]
        cars = sorted(cars)
        stack = []

        print(cars)
        for p,s in cars[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)