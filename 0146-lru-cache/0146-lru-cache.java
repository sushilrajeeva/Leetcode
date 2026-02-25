class Node {
        private int key;
        private int value;
        private Node previous;
        private Node next;
        
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }

        public int getKey() {
            return this.key;
        }

        public int getValue() {
            return this.value;
        }

        public void setKey(int key) {
            this.key = key;
        }
        public void setValue(int value) {
            this.value = value;
        }

        public Node getPreviousNode() {
            return this.previous;
        }
        
        public Node getNextNode() {
            return this.next;
        }

        public void setPreviousNode(Node node) {
            this.previous = node;
        }

        public void setNextNode(Node node) {
            this.next = node;
        }
    }

class LRUCache {

    private final int capacity;
    private final Map<Integer, Node> cache;
    private final Node head;
    private final Node tail;

    

    public LRUCache(int capacity) {

        this.capacity = capacity;

        this.cache = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);

        this.head.setNextNode(tail);
        this.tail.setPreviousNode(head);
        
    }

    public void moveToEnd(Node node) {

        Node lastNode = this.tail.getPreviousNode();

        lastNode.setNextNode(node);
        node.setPreviousNode(lastNode);

        node.setNextNode(this.tail);
        this.tail.setPreviousNode(node);
    }

    public void rewirePointers(Node node) {
        
        Node before = node.getPreviousNode();
        Node after = node.getNextNode();

        before.setNextNode(after);
        after.setPreviousNode(before);

        node.setPreviousNode(null);
        node.setNextNode(null);

    }
    
    public int get(int key) {

        if (!this.cache.containsKey(key)) {
            return -1;
        }

        Node node = this.cache.get(key);
        int value = node.getValue();

        this.rewirePointers(node);
        this.moveToEnd(node);

        return value;
        
    }
    
    public void put(int key, int value) {

        Node node = null;
        if (this.cache.containsKey(key)) {
            node = this.cache.get(key);
            node.setValue(value);
            this.rewirePointers(node);
        } else {
            node = new Node(key, value);
        }

        this.cache.put(key, node);
        this.moveToEnd(node);

        if (this.cache.size() > this.capacity) {
            Node lruNode = this.head.getNextNode();
            this.rewirePointers(lruNode);
            this.cache.remove(lruNode.getKey());
        }
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */