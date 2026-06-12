# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return 'N'
        preorder = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur: preorder.append('N')
            else:
                preorder.append(str(cur.val))
                stack.append(cur.right)
                stack.append(cur.left)
        print(preorder)
        return ','.join(preorder)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        datas = data.split(',')
        self.i = -1

        def dfs():
            self.i += 1
            if datas[self.i] == 'N': return None
            else:
                node = TreeNode(datas[self.i])
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs() 
