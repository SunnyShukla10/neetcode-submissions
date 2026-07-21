# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def dfs(node, max_val_path):
            if not node:
                return 0

            res = 1 if node.val >= max_val_path else 0 
            max_val_path = max(max_val_path, node.val)
            res += dfs(node.left, max_val_path)
            res += dfs(node.right, max_val_path)
            
            return res
        
        return dfs(root, root.val)
