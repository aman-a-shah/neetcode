class Node: 
    val: str
    nxt: list
    is_end: bool

    def __init__(self, val = ''):
        self.val = val
        self.nxt = []
        self.is_end = False

class PrefixTree:

    head: Node

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        cur = self.head
        for let in word:
            old = cur
            for neighbour in cur.nxt:
                if neighbour.val == let:
                    cur = neighbour
                    break
            if cur == old:
                cur.nxt.append(Node(let))
                cur = cur.nxt[-1]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.head
        for let in word:
            old = cur
            for neighbour in cur.nxt:
                if neighbour.val == let:
                    cur = neighbour
                    break
            if cur == old:
                return False
        return cur.is_end == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for let in prefix:
            old = cur
            for neighbour in cur.nxt:
                if neighbour.val == let:
                    cur = neighbour
                    break
            if cur == old:
                return False
        return True
        