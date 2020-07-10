class Solution(object):
    def totalNQueens(self, n):
        if n == 0:
            return 0
        res = [0]
        board = [['.'] * n for t in range(n)]
        self.do_solveNQueens(res, board, n)
        return res[0]
    
    def do_solveNQueens(self, res, board, num):
        if num == 0:
            res[0] += 1
            return
        ls = len(board)
        pos = ls - num
        check = [True] * ls
        for i in range(pos):
            for j in range(ls):
                if board[i][j] == 'Q':
                    check[j] = False
                    step = pos - i
                    if j + step < ls:
                        check[j + step] = False
                    if j - step >= 0:
                        check[j - step] = False
                    break
        if pos == 0:
            for j in range(int(ls / 2)):
                if check[j]:
                    board[pos][j] = 'Q'
                    self.do_solveNQueens(res, board, num - 1)
                    board[pos][j] = '.'
            res[0] *= 2
            if ls % 2 != 0:
                if check[int(ls / 2)]:
                    board[pos][int(ls / 2)] = 'Q'
                    self.do_solveNQueens(res, board, num - 1)
                    board[pos][int(ls / 2)] = '.'
        else:
            for j in range(ls):
                if check[j]:
                    board[pos][j] = 'Q'
                    self.do_solveNQueens(res, board, num - 1)
                    board[pos][j] = '.'