class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.capacity = k
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.count += 1
        self.queue[self.rear] = value
        if self.rear != self.capacity-1:
            self.rear += 1
        else:
            self.rear = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.count -= 1
        self.queue[self.front] = 0
        if self.front != self.capacity-1:
            self.front = self.front+1
        else:
            self.front = 0
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear-1]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()