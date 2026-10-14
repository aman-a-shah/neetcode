from collections import OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}      # key -> value
        self.freq = {}       # key -> frequency
        self.freq_keys = {}  # frequency -> OrderedDict of keys (acts as ordered set)
        self.min_freq = 0
    
    def _update_freq(self, key):
        """Update frequency of a key"""
        f = self.freq[key]
        
        # Remove key from its current frequency group
        del self.freq_keys[f][key]
        
        # If that frequency group is now empty and it was the min, bump min_freq
        if f == self.min_freq and not self.freq_keys[f]:
            self.min_freq += 1
        
        # Add key to the next frequency group (create it if needed)
        new_f = f + 1
        if new_f not in self.freq_keys:
            self.freq_keys[new_f] = OrderedDict()
        self.freq_keys[new_f][key] = None
        
        # Update freq map
        self.freq[key] = new_f
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self._update_freq(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.cache:
            # Update existing key's value and frequency
            self.cache[key] = value
            self._update_freq(key)
            return
        
        # Evict if at capacity
        if len(self.cache) >= self.capacity:
            # Pop the least recently used key within the min frequency group
            evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
            del self.cache[evict_key]
            del self.freq[evict_key]
        
        # Add new key with frequency 1
        self.cache[key] = value
        self.freq[key] = 1
        if 1 not in self.freq_keys:
            self.freq_keys[1] = OrderedDict()
        self.freq_keys[1][key] = None
        self.min_freq = 1