class MyHashMap:

    hs_mp = {}

    def __init__(self):
        self.hs_mp = {}

    def put(self, key: int, value: int) -> None:
        self.hs_mp[key] = value

    def get(self, key: int) -> int:
        if key in self.hs_mp:
            return self.hs_mp[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hs_mp:
            self.hs_mp.pop(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)