class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                res = stack.pop() + stack.pop() 
                stack.append(res)
            elif t == "-":
                a, b = stack.pop(),  stack.pop()
                stack.append(b-a)

            elif t == "*":
                res = stack.pop() * stack.pop()
                stack.append(res)
            elif t == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(t))
        return stack[-1]