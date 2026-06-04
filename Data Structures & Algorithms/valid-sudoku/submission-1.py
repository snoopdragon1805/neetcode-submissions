class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        rowDict={}
        colDict={}
        sqrDict=defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]!=".":
                    if(board[i][j] in sqrDict[(i//3,j//3)]):
                        return False
                    sqrDict[(i//3,j//3)].add(board[i][j])
                    rowDict[board[i][j]] = rowDict.get(board[i][j],0)+1
                    if rowDict[board[i][j]] > 1:
                        return False
                if board[j][i]!=".":
                    colDict[board[j][i]] = colDict.get(board[j][i],0)+1
                    if colDict[board[j][i]] > 1:
                        return False
            rowDict={}
            colDict={}
        return True

        