"""Maximum Frequency Stack"""
from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.vals = defaultdict(deque)
        self.max_f = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        self.vals[freq].append(val)
        self.max_f = max(self.max_f, freq)

    def pop(self) -> int:
        val = self.vals[self.max_f].pop()
        self.freq[val] -= 1
        if not self.vals[self.max_f]:
            del self.vals[self.max_f]
            self.max_f -= 1
        return val
