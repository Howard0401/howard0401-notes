# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        if not root1:
            return root2
        if not root2:
            return root1

        queue = deque()
        queue.append(root1)
        queue.append(root2)

        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
                
        return root1 
        
        # recursive
        # if root1 == None:
        #     return root2
        # if root2 == None:
        #     return root1
        # root1.val = root1.val + root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1