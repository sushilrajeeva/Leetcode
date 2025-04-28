class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, value) in self.bucket:
            if k == key:
                return value
        return -1
    
    def update(self, key, value):
        found = False
        for index, item in enumerate(self.bucket):
            if key == item[0]:
                self.bucket[index] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def remove(self, key):
        for index, item in enumerate(self.bucket):
            if key == item[0]:
                del self.bucket[index]
    


class MyHashMap:

    def __init__(self):
        self.key_mod = 2069
        self.hashMap = [Bucket()] * self.key_mod
        

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_mod
        self.hashMap[hash_key].update(key, value)
        

    def get(self, key: int) -> int:
        hash_key = key % self.key_mod
        return self.hashMap[hash_key].get(key)
        

    def remove(self, key: int) -> None:
        hash_key = key % self.key_mod
        self.hashMap[hash_key].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)