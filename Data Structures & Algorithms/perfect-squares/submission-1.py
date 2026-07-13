class Solution:
    def numSquares(self, n: int) -> int:
        while n%4==0:
            n//=4
        
        if n%8==7:
            return 4
        
        def isSquare(n):
            s = int(math.sqrt(n))
            return s*s == n
        
        if isSquare(n):
            return 1
        
        i=1
        while i*i<=n:
            if isSquare(n-i*i):
                return 2
            i+=1
        
        return 3
