class DynamicArray:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        if self.cap > 0:
            self.arr = [None] * self.cap

    def get(self, i: int) -> int:
        if i < self.cap:
            return self.arr[i]
        return None

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.cap:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        print(self.size)
        temp = self.arr[self.size]
        return temp

    def resize(self) -> None:
        self.cap = 2 * self.cap
        temp = [None] * self.cap
        for element in range(len(self.arr)):
            temp[element] = self.arr[element]
        self.arr = temp
        print(self.arr)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap