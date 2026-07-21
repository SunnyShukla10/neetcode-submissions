# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # keep iterating until the root and subroot are the same and then from there see if the values are the same

        # stack = [(root, subtree_head)]
        
        # while stack:
        #     r, s = stack.pop()
            
        #     if r.val == s.val:
        #         # check if the values below are the same 
                
        #     else:
        #         stack.append([r.left, s])
        #         stack.append([r.right, s])

        # Recursive DFS 
        
        
        # need to iterate the tree until we find the node from 
        # root tree that is hte same as the root of the subtree
        def sameTree(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
    
        if root is None: 
            return False
        
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        

    
