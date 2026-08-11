class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}
        self.size = capacity
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left  
    
    def add(self, node):
        prev, next = self.right.prev, self.right 
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.add(self.mp[key])
            return self.mp[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key, value)    
        self.add(self.mp[key])

        if len(self.mp) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.mp[lru.key]


        




        
