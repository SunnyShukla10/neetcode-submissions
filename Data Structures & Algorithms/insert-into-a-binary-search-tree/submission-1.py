# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        # find the leaf node we will insert the value under
        node = self.findLeafNode(root, val)
        nodeToAdd = TreeNode(val)
        if val < node.val:
            node.left = nodeToAdd
        else:
            node.right = nodeToAdd
        
        return root

    def findLeafNode(self, curr, val):        
        while curr:
            print(curr.val)
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    return curr
            else:
                if curr.right:
                    curr = curr.right  
                else:
                    return curr
    
            

