# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        curr = 1
        def helper(root, counter):
            nonlocal curr
            if not root.left and not root.right:
                curr = max(counter, curr)
            elif not root.left:
                helper(root.right, counter+1)
            elif not root.right:
                helper(root.left, counter+1)
            else:
                helper(root.left, counter+1)
                helper(root.right, counter+1)
        helper(root, curr)
        return curr
        