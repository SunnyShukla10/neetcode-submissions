# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = [root] 
        while q:
            level = []
            curr = []
            for node in q:
                level.append(node.val)
                    
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
                    
            res.append(level)
            q = curr
        return res

            
