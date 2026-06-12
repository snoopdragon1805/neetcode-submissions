class FreqStack:

    def __init__(self):
        self.freq={}
        self.group = {}
        self.mfreq = 0        

    def push(self, val: int) -> None:
        fr = self.freq.get(val,0)+1
        self.freq[val] = fr
        self.mfreq = max(self.mfreq,fr)

        if fr not in self.group:
            self.group[fr] = []
        self.group[fr].append(val)

    def pop(self) -> int:
        res = self.group[self.mfreq].pop()
        self.freq[res]-=1

        if not self.group[self.mfreq]:
            self.mfreq-=1
        
        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()