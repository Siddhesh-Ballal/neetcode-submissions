# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> None:
        if root.val >= p.val and root.val <= q.val or root.val <= p.val and root.val >= q.val: 
            self.res = root
            return 
        elif root.val < p.val and root.val < q.val: self.traverse(root.right, p, q)
        elif root.val > p.val and root.val > q.val: self.traverse(root.left, p, q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root
        self.traverse(root, p, q)
        return self.res