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
                val1 = stack.pop()
                val2 = stack.pop()

                if val1 == 0:
                    stack.append(0)
                else:
                    stack.append(int(val2/val1))
                
            else:
                # normal num
                stack.append(int(tok))
        print(stack)
        return stack[-1] if stack else 0