"""
Day 11 - Diameter of Binary Tree
Leetode Easy Problem

Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

Example:
  Given a binary tree
            1
           / \
          2   3
         / \     
        4   5    
  Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: 
  The length of path between two nodes is represented by the number of edges between them.
"""

class Solution(object):
    def diameterOfBinaryTree(self, root: TreeNode) -> int: 
        def depth(root):
            nonlocal maxDiameter
            if not root: return 0
            
            left = depth(root.left)
            right = depth(root.right)
            currentDiameter = left + right
            
            maxDiameter = max(maxDiameter, currentDiameter)
            return max(left, right) + 1
        
        maxDiameter = 0
        depth(root)
        return maxDiameter
