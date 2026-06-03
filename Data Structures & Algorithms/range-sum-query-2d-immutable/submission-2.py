class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.prefix = [[0]*(C+1) for _ in range(R+1)]

        # precompute 2D prefix
        for r in range(1, R+1):
            pre = 0
            for c in range(1, C+1):
                pre += matrix[r-1][c-1]
                self.prefix[r][c] = pre + self.prefix[r-1][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        prefix = self.prefix
        return prefix[row2][col2] - prefix[row2][col1-1] - prefix[row1-1][col2] + prefix[row1-1][col1-1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)