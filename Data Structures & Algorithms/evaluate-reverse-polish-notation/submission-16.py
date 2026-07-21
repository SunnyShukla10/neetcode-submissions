class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for tok in tokens:
            
            if tok == "+":
                # add
                stack.append(stack.pop() + stack.pop())
            elif tok == "-":
                # sub
                stack.append(-(stack.pop() - stack.pop()))
            elif tok == "*":
                # multiply
                stack.append(stack.pop() * stack.pop())
            elif tok == "/":
                # divide
                a = stack.pop()
                b = stack.pop()

                stack.append(int(float(b)/a))
                
            else:
                # normal num
                stack.append(int(tok))
        print(stack)
        return stack[-1] if stack else 0