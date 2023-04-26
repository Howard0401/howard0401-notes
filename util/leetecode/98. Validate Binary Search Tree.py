# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     pre = None
    #     def _isValidBST(root):
    #         nonlocal pre

    #         if not root:
    #             return True
            
    #         is_left = _isValidBST(root.left)
    #         if pre and pre.val >= root.val: return False
    #         pre = root
    #         is_right = _isValidBST(root.right)

    #         return is_left and is_right
    #     return _isValidBST(root)

    # 這個迭代法最好理解
    def isValidBST(self, root: Optional[TreeNode]):
        que, pre = [], None
        while root or que:
            while root:
                que.append(root)
                root = root.left
            root = que.pop()
            if pre is None:
                pre = root.val
            else:
                if pre >= root.val: return False
                pre = root.val
            root = root.right
        return True
        
    # inorder 這個比較繞
    # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    #     st = []
    #     cur = root
    #     pre = None
    #     while cur or st:
    #         if cur:
    #             st.append(cur)
    #             cur = cur.left
    #         else:
    #             cur = st.pop()
    #             if pre and pre.val >= cur.val:
    #                 return False
    #             pre = cur
    #             cur = cur.right
    #     return True
