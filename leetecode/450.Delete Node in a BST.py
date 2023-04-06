# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left: return root.right
            if not root.right: return root.left
            node = root.right
            while node.left:
                node = node.left
            node.left = root.left
            root = root.right
        return root
    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    #     if not root: return root
    #     if root.val == key:
    #         if not root.right:
    #             return root.left
    #         tmp = root.right
    #         while tmp.left:
    #             tmp = tmp.left
    #         root.val, tmp.val = tmp.val, root.val

    #     root.left = self.deleteNode(root.left, key)
    #     root.right = self.deleteNode(root.right, key)
    #     return root