# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def limitCheck(self, root: Optional[TreeNode], leftmax: int, rightmax: int) -> bool:
        if not root: return True
        if root.val <= leftmax or root.val >= rightmax: return False
        return self.limitCheck(root.left, leftmax, root.val) and self.limitCheck(root.right, root.val, rightmax)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.limitCheck(root, float('-inf'), float('inf'))