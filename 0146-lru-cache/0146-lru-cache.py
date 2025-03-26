class Node:
    def __init__(self, value: int = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    # cap = 2
    # head: Node = Node(-1)
    # tail: Node = Node(-1)

    # head.next = tail
    # tail.prev = head

    # head <=> (2, 2) <=> (1, 1) <=> tail

    # add(node: Node):
    #     next: Node = head.next
    #     head.next = node
    #     node.prev = head
    #     node.next = next
    #     next.prev = node

    #     dict[key] = node 

    # del_node(node:Node) -> Node:
    #     prev_node = node.prev
    #     next_node = node.next
    #     prev_node.next = next_node
    #     next_node.prev = prev_node
    #     node.next = None
    #     node.prev = None
    #     return node

    # get(key) -> int:
    #     if key not in dict: return -1
    #     key, val = dict[key].val
    #     node: Node = del_node(dict[key])
    #     add(node)

    #     return val

    # put(key, val):
    #     if length == capacity:
    #         to_del: Node = tail.prev
    #         del_node(to_del)
    #         dict.remove(key)
    #     node: Node = Node((key, val))
    #     add(node)
    #     dict[key] = node
        

    # dict = { 
    #             1: <address>
    #             2: <address>
    #          }

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.head: Node = Node((-1, -1))
        self.tail: Node = Node((-1, -1))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.memo: dict = {}

    def del_node(self, node: Node) -> Node:
        prev_node: Node = node.prev
        next_node: Node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        return node

    def add_node(self, node: Node) -> Node:
        next: Node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        return node
        

    def get(self, key: int) -> int:
        if key not in self.memo: return -1
        node: Node = self.memo[key]
        self.del_node(node)
        # node.value = (key, value)
        self.add_node(node)

        return node.value[1]
        

    def put(self, key: int, value: int) -> None:
        if key in self.memo:
            # Update existing node and move it to the head.
            node = self.memo[key]
            self.del_node(node)
            node.value = (key, value)
            self.add_node(node)
        else:
            # If at capacity, remove the least recently used node.
            if len(self.memo) == self.capacity:
                to_del: Node = self.tail.prev
                self.del_node(to_del)
                self.memo.pop(to_del.value[0])
            # Create a new node and add it to the head.
            node = Node((key, value))
            self.add_node(node)
            self.memo[key] = node

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)