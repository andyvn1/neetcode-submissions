class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.key_map = {}
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.key_map:
            self.remove(self.key_map[key])
            self.add(self.key_map[key])
            return self.key_map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            self.remove(self.key_map[key])
        self.key_map[key] = ListNode(key, value)
        self.add(self.key_map[key])

        if len(self.key_map) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.key_map[lru.key]


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        before_last = self.right.prev

        before_last.next = node
        self.right.prev = node
        node.prev = before_last
        node.next = self.right


        
