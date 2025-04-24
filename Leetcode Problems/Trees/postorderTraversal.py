# Problem: 145. Binary Tree Postorder Traversal
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
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
    def postorderTraversal_resurssion(self, root: Optional[TreeNode]) -> List[int]:
        # recursion
        result = []
        def postorder(node: TreeNode):
            if node:
                postorder(node.left)
                postorder(node.right)
                result.append(node.val)
        postorder(root)
        return result   

# here trick is to add current node to stack with boolean value is node is already visited or not. 
# if its false then add it back to stack (isvisited true) along with its right and left node with initial value as false 
# else if its true then add it to result
    def postorderTraversal_iteration(self, root: Optional[TreeNode]) -> List[int]:
        # iteration
        stack, result = [(root, False)], []
        while stack:
            cur , isVisited = stack.pop()
            if cur:
                if isVisited:
                    result.append(cur.val)
                else:
                    stack.append((cur, True))
                    stack.append((cur.right, False))
                    stack.append((cur.left, False))
        return result