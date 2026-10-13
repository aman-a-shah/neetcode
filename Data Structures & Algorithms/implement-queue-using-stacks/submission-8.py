class MyQueue:

    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x: int) -> None:
        # Always push to s1
        self.s1.append(x)

    def pop(self) -> int:
        # Ensure s2 has the front element
        self._move()
        return self.s2.pop()

    def peek(self) -> int:
        # Ensure s2 has the front element
        self._move()
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
    
    def _move(self) -> None:
        # If s2 is empty, transfer all elements from s1 to s2
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())