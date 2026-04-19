class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head


    def isEmpty(self) -> bool:
        return self.head.next==self.tail
        

    def append(self, value: int) -> None:
        last = self.tail
        prevlast = self.tail.prev
        node = Node(value)
        prevlast.next = node
        node.prev = prevlast
        node.next = last
        last.prev = node
        

    def appendleft(self, value: int) -> None:
        start = self.head
        second = self.head.next
        node = Node(value)
        start.next = node
        node.prev = start
        node.next = second
        second.prev = node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        tail = self.tail
        val = self.tail.prev
        prev = self.tail.prev.prev
        prev.next = tail
        tail.prev = prev
        return val.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        head = self.head
        val = self.head.next
        nextt = self.head.next.next
        nextt.prev = head
        head.next = nextt
        return val.value
        
