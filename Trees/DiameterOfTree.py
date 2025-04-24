# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from Trees import TreeNode
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def getDiameter(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = getDiameter(node.left)
            right = getDiameter(node.right)
            self.diameter = max(self.diameter, left+right)
            return 1 + max(left, right)
        getDiameter(root)
        return self.diameter