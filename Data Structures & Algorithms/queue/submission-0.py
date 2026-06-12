class node:

    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        

class Deque:
    
    def __init__(self):
        self.left = node(0)
        self.right = node(0)
        self.left.next = self.right
        self.right.prev = self.left
    

    def isEmpty(self) -> bool:
        return self.left.next == self.right


    def append(self, value: int) -> None:
        # Append to Right
        newNode = node(value)
        newNode.prev = self.right.prev
        self.right.prev.next = newNode
        self.right.prev = newNode
        newNode.next = self.right

    def appendleft(self, value: int) -> None:
        # Append to Left
        newNode = node(value)
        newNode.next = self.left.next
        self.left.next.prev = newNode
        self.left.next = newNode
        newNode.prev = self.left


    def pop(self) -> int:
        # Pop from right
        if self.isEmpty(): return -1
        poppedVal = self.right.prev.val
        self.right.prev.prev.next = self.right
        self.right.prev = self.right.prev.prev
        return poppedVal


    def popleft(self) -> int:
        # Pop from left
        if self.isEmpty(): return -1
        poppedVal = self.left.next.val
        self.left.next.next.prev = self.left
        self.left.next = self.left.next.next
        return poppedVal
