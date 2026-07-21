# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        # if not root:
        #     return 0 

        # return max(1 + self.maxDepth(root.left), 1 + self.maxDepth(root.right))

        # Iterative DFS
        stack = []
        if root:
            stack = [[root,1]]
        
        depth = 0
        while stack:
            node, node_depth = stack.pop()
            depth = max(depth, node_depth)
            
            if node.right:
                stack.append([node.right, node_depth+1])
            if node.left:
                stack.append([node.left, node_depth+1])     

        # BFS
        # q = deque()
        # if root:
        #     q = deque([root]) 
        # depth = 0
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     depth+=1


        return depth