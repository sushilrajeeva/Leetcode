class Node {

    private int key;
    private int value;
    private Node previous;
    private Node next;

    Node(int key, int value) {
        this.key = key;
        this.value = value;
    }

    public int getKey() {return this.key;}
    public int getValue() {return this.value;}
    public void setKey(int key) {this.key = key;}
    public void setValue(int value) {this.value = value;}
    public Node getPreviousNode() {return this.previous;}
    public Node getNextNode() {return this.next;}
    public void setPreviousNode(Node previous) {this.previous = previous;}
    public void setNextNode(Node next) {this.next = next;}

}

class LRUCache {

    private int capacity;
    private Node head;
    private Node tail;
    private Map<Integer, Node> cache;

    public LRUCache(int capacity) {

        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);

        this.head.setNextNode(this.tail);
        this.tail.setPreviousNode(this.head);
        
    }

    private void moveToEnd(Node node) {
        Node lastNode = this.tail.getPreviousNode();

        lastNode.setNextNode(node);
        node.setPreviousNode(lastNode);

        node.setNextNode(this.tail);
        this.tail.setPreviousNode(node);
    }

    private void rewirePointers(Node node) {
        Node leftNode = node.getPreviousNode();
        Node rightNode = node.getNextNode();

        leftNode.setNextNode(rightNode);
        rightNode.setPreviousNode(leftNode);

        node.setNextNode(null);
        node.setPreviousNode(null);
    }
    
    public int get(int key) {

        Node node = this.cache.get(key);
        if (node == null) {return -1;}

        int value = node.getValue();

        this.rewirePointers(node);
        this.moveToEnd(node);

        return value;
        
    }
    
    public void put(int key, int value) {

        Node node = this.cache.get(key);

        if (node == null) {
            node = new Node(key, value);
        } else {
            node.setValue(value);
            this.rewirePointers(node);
        }

        this.cache.put(key, node);
        this.moveToEnd(node);

        while (this.cache.size() > this.capacity) {
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