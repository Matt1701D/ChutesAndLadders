import unittest
import Board

class Test_ChutesAndLadders(unittest.TestCase):

    #Test board size
    def test_BoardSize(self):
        #Arrange
        expBoardSize = 10        

        #Act
        myBoard = Board.Board(expBoardSize,2)
        rowSize = len(myBoard.GameBoard)
        colSize = len(myBoard.GameBoard[1])

        #Assert
        self.assertEqual(expBoardSize,rowSize,"Row Size not "+str(expBoardSize))
        self.assertEqual(rowSize,colSize,"Row Size and Col Size not equal")

    #Test chutes and ladders board setup
    def test_BoardCandL(self):
        #Arrage
        expCandLCount = 18

        #Act
        myBoard = Board.Board(10,2)
        actCandLCount = len(myBoard.CandLmap)

        #Assert
        self.assertEqual(expCandLCount,actCandLCount,"CandLmap count is wrong")

    #Test players inital setup
    def test_BoardCandL(self):
        #Arrage
        playerNum = 2
        expPlayerLoc = {0: [-1,-1],1: [-1,-1]}

        #Act
        myBoard = Board.Board(10,playerNum)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player start point is wrong")

    def test_MoveLeftToRight(self):
        #Arrage
        myBoard = Board.Board(10,2)
        expPlayerLoc = {0: [9,4],1: [-1,-1]}

        #Act
        myBoard.makeMove(0,5)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player initial move is wrong")

    def test_MoveLeftToRightUp(self):
        #Arrage
        myBoard = Board.Board(10,2)
        expPlayerLoc = {0: [8,8],1: [-1,-1]}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving left to right then up is wrong")

    def test_MoveRightToLeft(self):
        #Arrage
        myBoard = Board.Board(10,2)
        expPlayerLoc = {0: [8,2],1: [-1,-1]}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving right to right is wrong")

    def test_MoveRightToLeftUp(self):
        #Arrage
        myBoard = Board.Board(10,2)
        expPlayerLoc = {0: [7,3],1: [-1,-1]}

        #Act
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        myBoard.makeMove(0,6)
        actPlayerLoc = myBoard.PlayerLoc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player moving right to right then up is wrong")

if __name__ == '__main__':
    unittest.main()
