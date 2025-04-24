# Problem: Binary Tree Inorder Traversal (Leetcode 94)
# Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
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
    def inorderTraversal_recursion(self, root: Optional[TreeNode]) -> List[int]:
        # recursion
        result = []
        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result    

    def inorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach
        stack, result = [],[]
        cur_node = root
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            result.append(cur_node.val)
            cur_node = cur_node.right
        return result  