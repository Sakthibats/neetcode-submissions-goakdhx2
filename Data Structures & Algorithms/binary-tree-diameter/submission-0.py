# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def help(tree):
            nonlocal count
            if not tree:
                return 0
            left = help(tree.left)
            right = help(tree.right)
            count = max(count, right+left)
            return 1+max(left, right)
        help(root)
        return count
        