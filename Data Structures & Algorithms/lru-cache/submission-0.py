class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.tail = None
        self.head = None
        
    def _append(self, node):
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            prev_node = self.tail
            self.tail = self.tail.next
            self.tail.prev = prev_node
            
    def _remove(self, node):
        if node.next and node.prev:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        elif node.next:
            self.head = self.head.next
            self.head.prev = None
        elif node.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        
        node.prev = None
        node.next = None

    def get(self, key):
        if key not in self.cache:
            return -1
        
        cur_node = self.cache[key]
        self._remove(cur_node)
        self._append(cur_node)
        return cur_node.value

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
            cur_node = self.cache[key]
            cur_node.value = value
            self._append(cur_node   )
            
            
        elif len(self.cache) < self.capacity:
            self._append(Node(key, value))
            self.cache[key] = self.tail

        
        else:   
            self._append(Node(key, value))
            self.cache[key] = self.tail
            del self.cache[self.head.key]
            self._remove(self.head)