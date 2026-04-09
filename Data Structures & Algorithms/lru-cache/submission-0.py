class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nextt = None
        self.prev = None
    
    def __str__(self):
        return f"{self.key}, {self.val}"
            
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr = 0
        self.hash = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.nextt = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        node.prev.nextt = node.nextt
        node.nextt.prev = node.prev
        self.curr-=1

    def add(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.nextt = nxt.prev = node
        node.nextt, node.prev = nxt, prev
        self.curr+=1

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        else:
            temp = self.hash[key]
            self.remove(temp)
            self.add(temp)
            return temp.val

    def put(self, key: int, value: int) -> None:
        new = Node(key, value)
        if key in self.hash:
            temp = self.hash[key]
            self.hash[key] = new
            self.remove(temp)
            self.add(new)
        else:
            if (self.curr+1)>self.capacity:
                first = self.left.nextt
                self.hash.pop(first.key, None)
                self.hash[key] = new
                self.remove(first)
                self.add(new)
            else:
                self.hash[key] = new
                self.add(new)
                



