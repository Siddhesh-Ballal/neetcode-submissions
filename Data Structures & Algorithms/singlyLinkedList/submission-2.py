
class ListNode:
    def __init__(self, val = 0, nextNode = None):
        self.val = val
        self.next = nextNode


class LinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur != None:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        new  = ListNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next: self.tail = new

    def insertTail(self, val: int) -> None:
        newTail = ListNode(val)
        newTail.next = None
        self.tail.next = newTail
        self.tail = newTail

    def remove(self, index: int) -> bool:     
        i = 0
        cur = self.head
        while cur and i < index:
            i += 1
            cur = cur.next
        
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = list()
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        
