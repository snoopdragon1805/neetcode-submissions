class FreqStack:

    def __init__(self):
        self.stack = []
        self.freq = {}        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.freq[val] = self.freq.get(val,0)+1

    def pop(self) -> int:
        m = 0
        for i in self.freq:
            m = max(m, self.freq[i])
        li=[]
        while(self.freq.get(self.stack[-1])!=m):
            li.append(self.stack.pop())
        re = self.stack.pop()
        for i in range(len(li)):
            self.stack.append(li.pop())
        self.freq[re]-=1
        return re



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()