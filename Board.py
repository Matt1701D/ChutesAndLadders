import random

class Board:

    def __init__(self, boardSize, playerNum):
        self.boardSize = boardSize
        self.playerNum = playerNum
        self.CandLmap = {}
        self.player_loc = {}
        self.initBoard()

    def initBoard(self):
        self.gameBoard = [['_____'] * self.boardSize for x in range(self.boardSize)]

        # set players off the board
        for i in range(self.playerNum):
            self.player_loc[i+1] = [-1,-1]
        
        #insert chutes
        self.gameBoard[0][2] = 'CT1'
        self.gameBoard[2][2] = 'CB1'
        self.CandLmap["CT1"] = [2,2]

        self.gameBoard[0][5] = 'CT2'
        self.gameBoard[2][5] = 'CB2'
        self.CandLmap["CT2"] = [2,5]

        self.gameBoard[0][7] = 'CT3'
        self.gameBoard[2][7] = 'CB3'
        self.CandLmap["CT3"] = [2,7]

        self.gameBoard[3][1] = 'CT4'
        self.gameBoard[8][1] = 'CB4'
        self.CandLmap["CT4"] = [2,2]

        self.gameBoard[3][3] = 'CT5'
        self.gameBoard[4][0] = 'CB5'
        self.CandLmap["CT5"] = [4,0]

        self.gameBoard[4][4] = 'CT6'
        self.gameBoard[4][7] = 'CB6'
        self.CandLmap["CT6"] = [4,7]

        self.gameBoard[5][7] = 'CT7'
        self.gameBoard[7][5] = 'CB7'
        self.CandLmap["CT7"] = [7,5]

        self.gameBoard[5][8] = 'CT8'
        self.gameBoard[8][9] = 'CB8'
        self.CandLmap["CT8"] = [8,9]

        self.gameBoard[8][4] = 'CT9'
        self.gameBoard[9][5] = 'CB9'
        self.CandLmap["CT9"] = [9,5]

        #insert ladders
        self.gameBoard[0][0] = 'LT1'
        self.gameBoard[2][0] = 'LB1'
        self.CandLmap["LB1"] = [0,0]

        self.gameBoard[1][3] = 'LT2'
        self.gameBoard[7][7] = 'LB2'
        self.CandLmap["LB2"] = [1,3]

        self.gameBoard[0][9] = 'LT3'
        self.gameBoard[2][9] = 'LB3'
        self.CandLmap["LB3"] = [0,9]

        self.gameBoard[3][6] = 'LT4'
        self.gameBoard[4][9] = 'LB4'
        self.CandLmap["LB4"] = [3,6]

        self.gameBoard[5][1] = 'LT5'
        self.gameBoard[7][0] = 'LB5'
        self.CandLmap["LB5"] = [5,1]

        self.gameBoard[5][3] = 'LT6'
        self.gameBoard[6][4] = 'LB6'
        self.CandLmap["LB6"] = [5,3]

        self.gameBoard[6][2] = 'LT7'
        self.gameBoard[9][0] = 'LB7'
        self.CandLmap["LB7"] = [6,2]

        self.gameBoard[6][9] = 'LT8'
        self.gameBoard[9][8] = 'LB8'
        self.CandLmap["LB8"] = [6,9]

        self.gameBoard[8][6] = 'LT9'
        self.gameBoard[9][3] = 'LB9'
        self.CandLmap["LB9"] = [8,6]

    def makeMove(self,turn):
        spin = random.randint(1,6)
        print("You spun a " + str(spin))

        #move player
        #playerX = self.player_loc[turn][1]

    def printBoard(self):
        for row in self.gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")
        #for x,y in self.CandLmap.items():
        #    print(x,y)
        
