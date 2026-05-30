# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function: check if two trees are identical
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
        
        if not root:
            return False
        
        # If the current node matches subRoot, return True
        if isSameTree(root, subRoot):
            return True
        
        # Otherwise, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)