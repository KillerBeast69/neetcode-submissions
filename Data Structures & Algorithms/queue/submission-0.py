class node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = node(-1)
        self.tail = node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new = node(value)
        last = self.tail.prev
        last.next = new
        new.prev = last
        new.next = self.tail
        self.tail.prev = new

    def appendleft(self, value: int) -> None:
        new = node(value)
        first = self.head.next
        first.prev = new
        new.next = first
        new.prev = self.head
        self.head.next = new

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        last.prev.next = self.tail
        self.tail.prev = last.prev
        val = last.value
        last = None
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        first.next.prev = self.head
        self.head.next = first.next
        val = first.value
        first = None
        return val

