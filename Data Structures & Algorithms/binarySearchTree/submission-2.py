class TreeNode:
    def __init__(self, key = 0, val = 0, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root: 
            self.root = newNode
            return
        else:
            cur = self.root
            while True:
                if cur.key > key:
                    if not cur.left:
                        cur.left = newNode
                        return
                    cur = cur.left
                elif cur.key < key:
                    if not cur.right:
                        cur.right = newNode
                        return
                    cur = cur.right
                else:
                    cur.val = val
                    return

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if cur.key > key:
                if not cur.left:
                    return -1
                cur = cur.left
            elif cur.key < key:
                if not cur.right:
                    return -1
                cur = cur.right
            else:
                return cur.val
        return -1

    def getMin(self) -> int:
        if not self.root: return -1

        cur = self.root
        while cur and cur.left:
            if cur.left:
                cur = cur.left
        return cur.val

    def getMax(self) -> int:
        if not self.root: return -1

        cur = self.root
        while cur and cur.right:
            if cur.right:
                cur = cur.right
        return cur.val


    def remove(self, key: int) -> None:
        
        def minNode(cur):
            while cur and cur.left:
                cur = cur.left
            return cur

        def rem(cur, key):
            if not cur: return None
            if cur.key > key:
                cur.left = rem(cur.left, key)
            elif cur.key < key:
                cur.right = rem(cur.right, key)
            else:
                if not cur.left: return cur.right
                elif not cur.right: return cur.left
                else:
                    inordersuccessor = minNode(cur.right)
                    cur.key = inordersuccessor.key 
                    cur.val = inordersuccessor.val
                    cur.right = rem(cur.right, inordersuccessor.key)
            return cur

        self.root = rem(self.root, key)
        

    def getInorderKeys(self) -> List[int]:
        res = []
        def inorder(node, res):
            if not node: return
            inorder(node.left, res)
            res.append(node.key)
            inorder(node.right, res)
        inorder(self.root, res)
        return res