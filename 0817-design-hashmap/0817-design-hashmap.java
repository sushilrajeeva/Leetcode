class Pair <U, V> {
    public U first;
    public V second;

    public Pair(U first, V second) {
        this.first = first;
        this.second = second;
    }
}

class Bucket {
    private ArrayList<Pair<Integer, Integer>> bucket;
    public Bucket() {
        this.bucket = new ArrayList<>();
    }

    public void update(int key, int value) {
        boolean found = false;
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                found = true;
                pair.second = value;
                break;
            }
        }
        if (!found) {
            this.bucket.add(new Pair<Integer, Integer>(key, value));
        }
    }

    public int get(int key) {
        boolean found = false;
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                return pair.second;
            }
        }
        return -1;
    }

    public void remove(int key) {
        for (Pair<Integer, Integer> pair : this.bucket) {
            if (pair.first.equals(key)) {
                this.bucket.remove(pair);
                break;
            }
        }
    }
}


class MyHashMap {
    private int key_mod;
    private List<Bucket> hash_map;
    public MyHashMap() {
        this.key_mod = 2069;
        this.hash_map = new ArrayList<Bucket>();
        for (int i = 0; i < this.key_mod; i++) {
            this.hash_map.add(new Bucket());
        }
    }
    
    public void put(int key, int value) {
        int hash_key = key % this.key_mod;
        this.hash_map.get(hash_key).update(key, value);
    }
    
    public int get(int key) {
        int hash_key = key % this.key_mod;
        return this.hash_map.get(hash_key).get(key);
    }
    
    public void remove(int key) {
        int hash_key = key % this.key_mod;
        this.hash_map.get(hash_key).remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */