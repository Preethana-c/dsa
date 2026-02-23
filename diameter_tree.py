# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # store the maximum diameter
        
        def height(node):
            if not node:
                return 0
            # Recursively get height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Update diameter at this node
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return height of subtree rooted at this node
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter