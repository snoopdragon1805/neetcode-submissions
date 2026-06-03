class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum=0
        i=row1
        j=col1
        while(i<=row2):
            while(j<=col2):
                sum += self._matrix[i][j]
                j+=1
            i+=1
            j=col1
        return sum        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)