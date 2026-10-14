from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}                       # key -> value
        self.freq_map = defaultdict(OrderedDict)  # freq -> OrderedDict{key: None}
        self.key_freq = {}                      # key -> freq
        self.min_freq = 0

    def _bump(self, key):
        f = self.key_freq[key]
        del self.freq_map[f][key]               # remove from old floor
        if not self.freq_map[f] and f == self.min_freq:
            self.min_freq += 1
        self.key_freq[key] = f + 1
        self.freq_map[f + 1][key] = None        # add to new floor (most recent = end)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        self._bump(key)
        return self.key_map[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_map:
            self.key_map[key] = value
            self._bump(key)
            return
        if len(self.key_map) == self.capacity:
            # evict LRU within the least-frequent floor = first item
            evict_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.key_map[evict_key]
            del self.key_freq[evict_key]
        self.key_map[key] = value
        self.key_freq[key] = 1
        self.freq_map[1][key] = None
        self.min_freq = 1