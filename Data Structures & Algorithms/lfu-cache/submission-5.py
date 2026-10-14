from collections import OrderedDict, defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = {} 
        self.key_freq = {}
        self.freq_key = defaultdict(OrderedDict) # dict of OrderedDict of key/val
        self.min_freq = float('inf')

    def get(self, key: int) -> int:
        if key not in self.key_val:
            return -1
        
        # update freq
        old_freq = self.key_freq[key]
        self.key_freq[key] += 1

        # delete from old bucket and move into new
        self.freq_key[old_freq].pop(key)
        self.freq_key[old_freq+1][key] = None

        if not self.freq_key[old_freq] and self.min_freq == old_freq:
            self.min_freq += 1
            
        return self.key_val[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_val:
            self.key_val[key] = value
            
            # update freq
            old_freq = self.key_freq[key]
            self.key_freq[key] += 1

            # delete from old bucket and move into new
            self.freq_key[old_freq].pop(key)
            self.freq_key[old_freq+1][key] = None

            if not self.freq_key[old_freq] and self.min_freq == old_freq:
                self.min_freq += 1
        elif len(self.key_val) < self.capacity:
            self.key_val[key] = value
            
            # update freq
            self.key_freq[key] = 1

            # delete from old bucket and move into new
            self.freq_key[1][key] = value

            self.min_freq = min(self.min_freq, 1)
        else:
            # need to pop one
            old_key, _ = self.freq_key[self.min_freq].popitem(last=False)
            
            old_freq = self.key_freq[old_key]
            self.key_freq.pop(old_key)
            self.key_val.pop(old_key)

            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_key[1][key] = None
            
            self.min_freq = 1

