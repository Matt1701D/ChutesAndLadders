import unittest
import Board

class Test_ChutesAndLadders(unittest.TestCase):

    #Test board size
    def test_BoardSize(self):
        #Arrange
        expBoardSize = 10        

        #Act
        myBoard = Board.Board(expBoardSize,2)
        rowSize = len(myBoard.gameBoard)
        colSize = len(myBoard.gameBoard[1])

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
        expPlayerLoc = {1: [-1,-1],2: [-1,-1]}

        #Act
        myBoard = Board.Board(10,playerNum)
        actPlayerLoc = myBoard.player_loc

        #Assert
        self.assertEqual(expPlayerLoc,actPlayerLoc,"Player start point is wrong")

if __name__ == '__main__':
    unittest.main()
