class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.mapa = {}
        self.left = ListNode(-1, -1)
        self.right = ListNode(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
                

    def get(self, key: int) -> int:
        if key in self.mapa:
            self.remove(self.mapa[key])
            self.add(self.mapa[key])
            return self.mapa[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mapa:
            self.remove(self.mapa[key])
        self.mapa[key] = ListNode(key, value)
        self.add(self.mapa[key])

        if len(self.mapa) > self.size:
            LRU = self.left.next
            self.remove(LRU)
            del self.mapa[LRU.key]

    def add(self, node):
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


        
