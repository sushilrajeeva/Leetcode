class Node:
    """Node for doubly linked list - represents a key-value pair"""
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = prev
        self.next = None

class DoublyLinkedList:
    """Doubly linked list to maintain keys at same frequency in LRU order"""
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node) -> None:
        """Add node right after head (most recently used)"""
        nextNode = self.head.next
        node.next = nextNode
        node.prev = self.head
        nextNode.prev = node
        self.head.next = node

        self.size += 1

    def remove_node(self, node: Node) -> None:
        """Remove a specific node from the list"""
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = None
        node.prev = None
        self.size -= 1

    def remove_from_tail(self) -> Node:
        """Remove and return the least recently used node (before tail)"""
        if self.size == 0:
            return None

        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self.size == 0


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        
        # Key -> Node
        self.key_to_node = {}

        # Frequency -> DoublyLinkedList (maintains LRU order from same frequency)
        self.freq_to_list = {}

    def _update_frequency(self, node: Node) -> None:
        """Helper: update frequency when a node is accessed"""
        freq = node.freq

        # remove node from current frequency list
        self.freq_to_list[freq].remove_node(node)

        if self.freq_to_list[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1

        node.freq += 1
        new_freq = node.freq

        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        self.freq_to_list[new_freq].add_to_head(node)

    def _evict_lfu(self) -> None:
        """Helper: Evict the least frequently used key (with LRU tiebreaker)"""
        # Get the LFU list
        lfu_list = self.freq_to_list[self.min_freq]
        
        # Remove the tail (least recently used among least frequent)
        evict_node = lfu_list.remove_from_tail()
        
        # Remove from cache
        del self.key_to_node[evict_node.key]


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1

        # Get the node
        node = self.key_to_node[key]

        # Update the frequency since we accessed this key
        self._update_frequency(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        # Case 1: Key already exists - update value and frequency
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_frequency(node)
            return
        
        # Case 2: Cache is full - evict LFU before inserting
        if len(self.key_to_node) >= self.capacity:
            self._evict_lfu()
        
        # Case 3: Insert new key with frequency 1
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        
        # Add to frequency 1 list
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()
        self.freq_to_list[1].add_to_head(new_node)
        
        # New key always has frequency 1
        self.min_freq = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)