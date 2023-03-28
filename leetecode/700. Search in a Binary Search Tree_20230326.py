# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # res = None
        # if not root or root.val == val:
        #     return root
        # if root.val > val:
        #     res = self.searchBST(root.left, val)
        # if root.val < val:
        #     res = self.searchBST(root.right,val)
        # return res
        while root is not None:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None
