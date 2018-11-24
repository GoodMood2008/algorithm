#!/user/bin/python
#-*- coding:utf-8 -*-




class Node:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.option = []
        self.c = '.'


class Solution1:
    def solveSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if None == board or len(board) == 0:
            return False
        self.solve(board)

    def solve1(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in ['1','2','3','4','5','6', '7', '8', '9']:
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if (self.solve(board)):
                                return True
                            else:
                                board[i][j] = '.'
        return False

    def isValid1(self, board, row, col, c):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if i == row and board[i][j] == c:
                    return False
                if j == col and board[i][j] == c:
                    return False

                row_min = int(row/3) * 3
                col_min = int(col/3) * 3
                if row_min <= i < (row_min + 3) and \
                   col_min <= j < (col_min + 3) and \
                   board[i][j] == c:
                   return False
        return True


class Solution:
    def __init__(self):
        self.validValues = ['1','2','3','4','5','6', '7', '8', '9']
        self.cols = []
        self.rows = []
        self.squares = []
        self.nodes = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if None == board or len(board) == 0:
            return
        self.preProcess(board)
        for node in self.nodes:
            if node.c == '.':
                print(node.i, " ", node.j, " ", node.option)            
        #self.solve(board)

        
    def preProcess(self, board):
        for _ in range(9):
            self.cols.append([])
            self.rows.append([])
            self.squares.append([])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                self.rows[i].append(board[i][j])
                self.cols[j].append(board[i][j])
                self.squares[self.squareIndex(i, j)].append(board[i][j])

        # find all the node need to fill and its options
        # this is the first o
        nodedict = dict()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    node = Node(i, j)
                    exist = set(self.rows[i] + self.cols[j] + self.squares[self.squareIndex(i, j)])
                    node.option = list(filter(lambda a : a not in exist, self.validValues))
                    # add to dict                
                    nodedict.update({(i, j):node})

        #if node.option == 1, the value is fix, update it recursively
        self.updateFixOption(nodedict, board)

        self.nodes = sorted(nodedict.values(), key=lambda node : len(node.option))

    def squareIndex(self, i, j):
        return int(i/3) * 3 + int(j/3)

    #if node.option == 1, the value is fix
    def updateFixOption(self, nodedict, board):
        fixNodes = list(filter(lambda node: len(node.option) == 1, nodedict.values()))
        if not fixNodes:
            return

        #fix iter process as people's thinking style
        #fill in board and remove
        for fixnode in fixNodes:
            fix = fixnode.option[0]
            board[fixnode.i][fixnode.j] = fix #fix ele
            nodedict.pop((fixnode.i, fixnode.j)) #remove fix node from dict
            self.rows[fixnode.i].append(fix) #update rows, add the fix
            self.cols[fixnode.j].append(fix) #udpate cols, add the fix
            self.squares[self.squareIndex(fixnode.i, fixnode.j)].append(fix) #update square, add the fix

        #update the remain nodes, remove fix from relate node
        for fixnode in fixNodes:
            fix = fixnode.option[0]        
            #update other node, remove the option
            for pos in range(9):
                node = nodedict.get((fixnode.i, pos))
                if None != node and fix in node.option:
                    node.option.remove(fix)
            for pos in range(9):
                node = nodedict.get((pos, fixnode.j))
                if None != node and fix in node.option:
                    node.option.remove(fix)
            squareI = int(fixnode.i/3) * 3
            squareJ = int(fixnode.j/3) * 3
            for i in range(squareI, squareI + 3):
                for j in range(squareJ, squareJ + 3):
                    node = nodedict.get((i, j))
                if None != node and fix in node.option:
                    node.option.remove(fix)           

        # do more until there are no more node with len(option) == 1     
        self.updateFixOption(nodedict, board)

    # this will be more faster than the Solution1 is
    def isValid(self, board, row, col, c):
        for num in range(9):
            if board[row][num] != '.' and board[row][num] == c:
                return False
            if board[num][col] != '.' and board[num][col] == c:
                return False

        squareI = int(row/3) * 3
        squareJ = int(col/3) * 3
        for i in range(squareI, squareI + 3):
            for j in range(squareJ, squareJ + 3):
                value = board[i][j]
                if value != '.' and value == c:
                    return False 
        return True

    # if too many node, the recursive is too deep, it cusume a lot of time to recursive
    def solve(self, board):     
        for node in self.nodes:
            if node.c == '.':
                print(node.i, " ", node.j, " ", node.option)
                for c in node.option:
                    if self.isValid(board, node.i, node.j, c):
                        # update state
                        board[node.i][node.j] = c
                        node.c = c         
                        if (self.solve(board)):
                            return True
                        else:
                            #recover sate
                            board[node.i][node.j] = '.'
                            node.c = '.'                    
        return False


#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
import unittest
class SolutionTest(unittest.TestCase):
    def testSolution(self):
        solution1 = Solution1()
        inputdata = [["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]
        outputdata = [["5","3","4","6","7","8","9","1","2"],
                      ["6","7","2","1","9","5","3","4","8"],
                      ["1","9","8","3","4","2","5","6","7"],
                      ["8","5","9","7","6","1","4","2","3"],
                      ["4","2","6","8","5","3","7","9","1"],
                      ["7","1","3","9","2","4","8","5","6"],
                      ["9","6","1","5","3","7","2","8","4"],
                      ["2","8","7","4","1","9","6","3","5"],
                      ["3","4","5","2","8","6","1","7","9"]]
        self.assertTrue(not solution1.isValid1(inputdata, 0, 2, '8'))
        self.assertTrue(not solution1.isValid1(inputdata, 0, 2, '5'))
        self.assertTrue(solution1.isValid1(inputdata, 0, 2, '4'))
        solution = Solution()
        #solution.solveSudoku(inputdata)
        #print(inputdata)
        #self.assertTrue(inputdata == outputdata)

        input = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
        solution.solveSudoku(input)
        print(input)
      
if __name__ == "__main__" : unittest.main()
