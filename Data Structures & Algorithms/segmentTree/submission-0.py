class Node:
    def __init__(self, l: int, r: int, total: int):
        self.total = total
        # Children
        self.left, self.right = None, None
        # Range
        self.l, self.r = l, r

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: List[int], l: int, r: int) -> Node:
        if l == r: return Node(l, r, nums[l])

        root = Node(l, r, 0)
        m = (l + r) // 2
        root.left = self.build(nums, l, m) 
        root.right = self.build(nums, m + 1, r)
        root.total = root.left.total + root.right.total

        return root
    
    
    def update(self, index: int, val: int) -> None:
        self.update_helper(self.root, index, val)

    def update_helper(self, root: Node, index: int, val: int) -> None:
        if root.l == root.r:
            root.total = val
            return

        m = (root.l + root.r) // 2
        if index > m: self.update_helper(root.right, index, val)
        else: self.update_helper(root.left, index, val)
        root.total = root.left.total + root.right.total
        

    def query(self, L: int, R: int) -> int:
        return self.query_helper(self.root, L, R)

    def query_helper(self, root: Node, L: int, R: int) -> int:
        if root.r < L or root.l > R : return 0  # Out of range
        if root.l >= L and root.r <= R: return root.total   # within range
        return (self.query_helper(root.left, L, R) + self.query_helper(root.right, L, R))
