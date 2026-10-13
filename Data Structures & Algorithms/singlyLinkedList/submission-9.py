class Node:
    val: int
    nxt: Node

    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt

class LinkedList:

    def __init__(self):
        self.arr = []
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr is not None: 
            if i == index:
                return curr.val
            i += 1
            curr = curr.nxt
        return -1

    def insertHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def insertTail(self, val: int) -> None:
        curr = self.head
        if not curr:
            self.head = Node(val)
            return
        while curr.nxt is not None: 
            curr = curr.nxt
        curr.nxt = Node(val)

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head 
        prev = None

        if index == 0:
            if self.head:
                self.head = self.head.nxt
                return True
            else:
                return False

        while curr is not None: 
            if i == index:
                prev.nxt = curr.nxt
                return True
            i += 1
            prev = curr
            curr = curr.nxt
            
        return False

    def getValues(self) -> List[int]:
        acc = []

        curr = self.head
        while curr:
            acc.append(curr.val)
            curr = curr.nxt

        return acc
