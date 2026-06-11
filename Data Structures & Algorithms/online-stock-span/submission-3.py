class StockSpanner:

    def __init__(self):
        # FIX: Correctly initialize a persistent stack instance variable
        self.stack = []        

    def next(self, price: int) -> int:
        # Start with a base span of 1 for the current day
        span = 1
        
        # Collapse smaller or equal prices into the current day's span
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        # Push the current price and its total accumulated span onto the stack
        self.stack.append((price, span))
        
        return span
