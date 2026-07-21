# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # DFS
        
        # formula is going to be 1 + height_left_subtree + height_subtree
        # global variable we keep updating

        self.res = 0

        # a recursive function that will find diameter
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)

        return self.res
