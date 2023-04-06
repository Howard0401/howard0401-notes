# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        parent = None

        def traverse(cur: TreeNode, val: int) -> None:
            nonlocal parent
            if not cur:
                new_node = TreeNode(val)
                if parent.val < val:
                    parent.right = new_node
                else:
                    parent.left = new_node
                return
            parent = cur
            if cur.val < val:
                traverse(cur.right, val)
            else:
                traverse(cur.left, val)
            return
        traverse(root, val)
        return root

    # def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if not root:
    #         return TreeNode(val)
        
    #     if val < root.val:
    #         root.left = self.insertIntoBST(root.left, val)
        
    #     if val > root.val:
    #         root.right = self.insertIntoBST(root.right, val)
        
    #     return root
