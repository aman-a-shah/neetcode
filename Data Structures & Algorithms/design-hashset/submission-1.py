class MyHashSet:

    hs_st = set()

    def __init__(self):
        self.hs_st = set()

    def add(self, key: int) -> None:
        self.hs_st.add(key)

    def remove(self, key: int) -> None:
        if key in self.hs_st:
            self.hs_st.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.hs_st


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)