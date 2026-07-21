# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            3
           / 
          3
         / \ 
        4   2 

        '''
        
        
        self.res = 0
        
        def dfs(node, max_value):
            if not node:
                return
            
            # check this node
            if node.val >= max_value:
                max_value = node.val
                self.res += 1
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, float("-inf"))
        return self.res 
