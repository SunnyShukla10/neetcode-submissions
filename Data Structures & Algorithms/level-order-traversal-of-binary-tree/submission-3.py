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
        
        q = deque([root])

        while q:
            nodes = []
            for _ in range(len(q)):
                n = q.popleft()
                nodes.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            res.append(nodes)
        
        return res
