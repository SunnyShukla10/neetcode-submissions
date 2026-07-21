# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        # if not p and not q:
        #     return True
        # elif p and q and p.val == q.val:
        #     return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        # else:
        #     return False
        

        # Iterative DFS
        # stack = [(p,q)]
        
        # while stack:
        #     p, q = stack.pop()

        #     if not p and not q:
        #         continue
        #     if not p or not q or p.val != q.val:             
        #         return False

        #     stack.append((p.left,q.left))
        #     stack.append((p.right,q.right))

        # BFS
        q1 = deque([q])
        q2 = deque([p])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            q1.append(n1.left)
            q1.append(n1.right)
            q2.append(n2.left)
            q2.append(n2.right)
        
 


        return True
            

