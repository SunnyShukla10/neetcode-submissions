class Solution:
    def simplifyPath(self, path: str) -> str:
        # we add each "directory" into the stack
        # when we reach a '..' we pop the top of the stack (if there is something in it)

        stack = []

        paths = path.split('/')


        for p in paths:
            if p == "" or p==".":
                continue
            
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
            
            

        return "/" + "/".join(stack) 