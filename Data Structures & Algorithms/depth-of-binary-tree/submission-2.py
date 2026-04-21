# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def help(root, cnt):
            if root:
                return max(help(root.left, cnt+1), help(root.right, cnt+1))
            else:
                return cnt
        return help(root, 0)