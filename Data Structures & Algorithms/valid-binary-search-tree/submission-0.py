# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.left

        if left == None and right == None:
            return True
        
        if left.val > right.val or root.val < left.val:
            return False

        return (self.isValidBST(left) and self.isValidBST(right))
        