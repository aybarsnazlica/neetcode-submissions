class MyHashMap:

    def __init__(self):
        self.buckets = [[] for _ in range(10**6 + 1)]

    def hash(self, key):
        return key % len(self.buckets)
    
    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        self.buckets[idx] = [value]
        
    def get(self, key: int) -> int:
        idx = self.hash(key)
        if not self.buckets[idx]:
            return -1
        return self.buckets[idx][0]

    def remove(self, key: int) -> None:
        idx = self.hash(key)
        self.buckets[idx] = None      


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
