class Node:
    """DLL node that represents a frequency bucket."""
    
    def __init__(self, freq: int):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.loc = {}

    def _insert_between(self, left: Node, right: Node, node: Node) -> None:
        """Insert node between left and right."""
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node

    def _insert_after(self, node: Node, new_node: Node) -> None:
        """Insert new_node right after node."""
        self._insert_between(node, node.next, new_node)
    
    def _insert_before(self, node: Node, new_node: Node) -> None:
        """Insert new_node right before node."""
        self._insert_between(node.prev, node, new_node)

    def _remove_node(self, node: Node) -> None:
        """Remove node from the DLL (node is guaranteed not to be head/tail)."""
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None  # optional, but nice for safety

    def _ensure_next_bucket(self, node: Node) -> Node:
        """
        Ensure there is a bucket with frequency node.freq + 1 directly after 'node'.
        Return that bucket.
        """
        next_node = node.next
        target_freq = node.freq + 1
        if next_node is self.tail or next_node.freq != target_freq:
            created = Node(target_freq)
            self._insert_after(node, created)
            return created
        return next_node

    def _ensure_prev_bucket(self, node: Node) -> Node:
        """
        Ensure there is a bucket with frequency node.freq - 1 directly before 'node'.
        Return that bucket.
        """
        prev_node = node.prev
        target_freq = node.freq - 1
        if prev_node is self.head or prev_node.freq != target_freq:
            created = Node(target_freq)
            self._insert_before(node, created)
            return created
        return prev_node

    def _ensure_bucket_1_at_front(self) -> Node:
        """
        Ensure the first real bucket (after head) is frequency 1. Return it.
        """
        first = self.head.next
        if first is self.tail or first.freq != 1:
            created = Node(1)
            self._insert_after(self.head, created)
            return created
        return first
        

    def inc(self, key: str) -> None:
        if key not in self.loc:
            # New key gets freq 1
            bucket1 = self._ensure_bucket_1_at_front()
            bucket1.keys.add(key)
            self.loc[key] = bucket1
            return

        # Move key from freq f to f+1
        curr = self.loc[key]
        curr.keys.remove(key)
        next_bucket = self._ensure_next_bucket(curr)
        next_bucket.keys.add(key)
        self.loc[key] = next_bucket

        # Clean up empty bucket
        if not curr.keys:
            self._remove_node(curr)

    def dec(self, key: str) -> None:
        if key not in self.loc:
            return

        curr = self.loc[key]
        curr.keys.remove(key)

        if curr.freq == 1:
            # Key disappears entirely
            del self.loc[key]
        else:
            # Move key from freq f to f-1
            prev_bucket = self._ensure_prev_bucket(curr)
            prev_bucket.keys.add(key)
            self.loc[key] = prev_bucket

        # Clean up empty bucket
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        # Tail.prev is the highest-frequency bucket (or head if empty)
        if self.tail.prev is self.head:
            return ""
        # Return any key from that bucket
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # Head.next is the lowest-frequency bucket (or tail if empty)
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()