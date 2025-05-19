class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity: int):
        self.root = {}
        self.root["head"] = Node("head",-1)
        self.root["tail"] = Node("tail",-2)
        self.root["head"].next = self.root["tail"]
        self.root["tail"].prev = self.root["head"]
        self.capacity = capacity
        self.size = 0

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, node):
        node.prev = self.root["tail"].prev
        node.next = self.root["tail"]
        self.root["tail"].prev.next = node
        self.root["tail"].prev = node

    
    def get(self, key: int) -> int:
        # Check if key exists
        if key not in self.root:
            return -1
        
        node = self.root[key]
        self.remove(node)
        self.add_to_tail(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        # If updating value of existing key, remove it and re-add it to the tail
        if key in self.root:
            self.root[key].val = value
            self.remove(self.root[key])
            self.add_to_tail(self.root[key])
            return

        new_node = Node(key, value)
        self.root[key] = new_node
        self.add_to_tail(new_node)
        self.size += 1

        if self.size > self.capacity:
            lru = self.root["head"].next
            self.remove(lru)
            self.root.pop(lru.key)
            self.size -= 1