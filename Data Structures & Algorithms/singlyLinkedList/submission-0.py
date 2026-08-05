class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.cur = None
        self.head = ListNode(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        self.cur = self.head.next
        while(index > 0 and self.cur):
            self.cur = self.cur.next
            index -= 1
        if self.cur:
            return self.cur.val
        return -1

    def insertHead(self, val: int) -> None:
        self.cur = ListNode(val)
        temp = self.head.next
        self.head.next = self.cur
        self.cur.next = temp
        if self.head == self.tail:
            self.tail = self.cur

    def insertTail(self, val: int) -> None:
        self.cur = ListNode(val)
        self.tail.next = self.cur
        self.tail = self.cur

    def remove(self, index: int) -> bool:
        prev = self.head
        self.cur = self.head.next
        while(index > 0 and self.cur):
            prev = self.cur
            self.cur = self.cur.next
            index -= 1
        if self.cur:
            prev.next = self.cur.next
            if self.cur == self.tail:
                self.tail = prev
            return True
        return False

    def getValues(self) -> List[int]:
        values = []
        self.cur = self.head.next
        while(self.cur):
            print(self.cur.val)
            values.append(self.cur.val)
            self.cur = self.cur.next
        return values