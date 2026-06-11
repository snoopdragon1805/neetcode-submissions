class StockSpanner:

    def __init__(self):
        self.arr=[]        

    def next(self, price: int) -> int:
        stack=[]
        stack[:] = self.arr
        res=1
        while stack and stack[-1]<=price:
            res+=1
            stack.pop()
        self.arr.append(price)
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)