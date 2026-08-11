class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mapa = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
    
    def get(self, key: int) -> int:
        if key in self.mapa:
            self.remove(self.mapa[key])
            self.insert(self.mapa[key])
            return self.mapa[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapa:
            self.remove(self.mapa[key])
        self.mapa[key] = Node(key, value)
        self.insert(self.mapa[key])

        if len(self.mapa) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.mapa[lru.key]
        
