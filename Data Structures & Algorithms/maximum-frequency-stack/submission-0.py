from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # val -> frequency
        self.group = defaultdict(list)  # frequency -> stack of values
        self.max_freq = 0
        
    def push(self, val: int) -> None:
        # Increment frequency
        self.freq[val] += 1
        f = self.freq[val]
        
        # Update max frequency
        self.max_freq = max(self.max_freq, f)
        
        # Add to the group for this frequency
        self.group[f].append(val)
        
    def pop(self) -> int:
        # Get the most recent element from the highest frequency group
        val = self.group[self.max_freq].pop()
        
        # Decrement frequency
        self.freq[val] -= 1
        
        # If this frequency group is empty, decrease max_freq
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return val