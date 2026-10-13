class MyQueue:
    def __init__(self):
        self.s1 = []  # input stack
        self.s2 = []  # output stack

    def push(self, x: int) -> None:
        self.s1.append(x)  # O(1)

    def pop(self) -> int:
        # If s2 is empty, transfer all from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())  # O(1) each
        return self.s2.pop()  # O(1)

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]  # O(1)

    def empty(self) -> bool:
        return not self.s1 and not self.s2