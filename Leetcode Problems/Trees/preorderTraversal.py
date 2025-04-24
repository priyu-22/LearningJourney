# Problem: Binary Tree Preorder Traversal (Leetcode 144)
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Difficulty: Easy
# Approach: Binary Tree Recursion and iteration
# Time: O(n), Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from Trees import TreeNode


class Solution:
    def preorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        # recursive
        result = []
        def preorder(node: TreeNode):
            if node: 
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)
        return result        

    def preorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach
        stack, result = [root],[]
        if root:
            while stack:
                node = stack.pop()
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result    