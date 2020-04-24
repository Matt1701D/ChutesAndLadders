class Board(object):

    def __init__(self, boardSize, playerNum):
        self.__boardSize = boardSize
        self.__playerNum = playerNum
        self.__gameBoard = []
        self.__CandLmap = {}
        self.__player_loc = {}

        self.__initBoard()

    # PROPERTIES

    @property
    def gameBoard(self):
        return self.__gameBoard

    @property
    def CandLmap(self):
        return self.__CandLmap

    @property
    def PlayerLoc(self):
        return self.__player_loc

    # PRIVATE METHODS

    # initialize the game board and players
    def __initBoard(self):
        self.__gameBoard = [['------'] * self.__boardSize for x in range(self.__boardSize)]

        # set players off the board
        for i in range(self.__playerNum):
            self.__player_loc[i] = [-1,-1]
        
        #insert chutes
        self.__gameBoard[0][2] = 'CT1---'
        self.__gameBoard[2][2] = 'CB1---'
        self.__CandLmap["CT1"] = [2,2]

        self.__gameBoard[0][5] = 'CT2---'
        self.__gameBoard[2][5] = 'CB2---'
        self.__CandLmap["CT2"] = [2,5]

        self.__gameBoard[0][7] = 'CT3---'
        self.__gameBoard[2][7] = 'CB3---'
        self.__CandLmap["CT3"] = [2,7]

        self.__gameBoard[3][1] = 'CT4---'
        self.__gameBoard[8][1] = 'CB4---'
        self.__CandLmap["CT4"] = [2,2]

        self.__gameBoard[3][3] = 'CT5---'
        self.__gameBoard[4][0] = 'CB5---'
        self.__CandLmap["CT5"] = [4,0]

        self.__gameBoard[4][4] = 'CT6---'
        self.__gameBoard[4][7] = 'CB6---'
        self.__CandLmap["CT6"] = [4,7]

        self.__gameBoard[5][7] = 'CT7---'
        self.__gameBoard[7][5] = 'CB7---'
        self.__CandLmap["CT7"] = [7,5]

        self.__gameBoard[5][8] = 'CT8---'
        self.__gameBoard[8][9] = 'CB8---'
        self.__CandLmap["CT8"] = [8,9]

        self.__gameBoard[8][4] = 'CT9---'
        self.__gameBoard[9][5] = 'CB9---'
        self.__CandLmap["CT9"] = [9,5]

        self.__gameBoard[1][6] = 'CT0---'
        self.__gameBoard[7][3] = 'CB0---'
        self.__CandLmap["CT0"] = [7,3]

        #insert ladders
        self.__gameBoard[0][0] = 'LT1---'
        self.__gameBoard[2][0] = 'LB1---'
        self.__CandLmap["LB1"] = [0,0]

        self.__gameBoard[1][3] = 'LT2---'
        self.__gameBoard[7][7] = 'LB2---'
        self.__CandLmap["LB2"] = [1,3]

        self.__gameBoard[0][9] = 'LT3---'
        self.__gameBoard[2][9] = 'LB3---'
        self.__CandLmap["LB3"] = [0,9]

        self.__gameBoard[3][6] = 'LT4---'
        self.__gameBoard[4][9] = 'LB4---'
        self.__CandLmap["LB4"] = [3,6]

        self.__gameBoard[5][1] = 'LT5---'
        self.__gameBoard[7][0] = 'LB5---'
        self.__CandLmap["LB5"] = [5,1]

        self.__gameBoard[5][3] = 'LT6---'
        self.__gameBoard[6][4] = 'LB6---'
        self.__CandLmap["LB6"] = [5,3]

        self.__gameBoard[6][2] = 'LT7---'
        self.__gameBoard[9][0] = 'LB7---'
        self.__CandLmap["LB7"] = [6,2]

        self.__gameBoard[6][9] = 'LT8---'
        self.__gameBoard[9][8] = 'LB8---'
        self.__CandLmap["LB8"] = [6,9]

        self.__gameBoard[8][6] = 'LT9---'
        self.__gameBoard[9][3] = 'LB9---'
        self.__CandLmap["LB9"] = [8,6]

    # PUBLIC METHODS

    # Compute the location for current move and move player
    def makeMove(self, turn, spin):
        #get player pos
        playerX = playerX_new = self.__player_loc[turn][1]
        playerY = playerY_new = self.__player_loc[turn][0]

        # Remember gameplay starts at bottom left of board (8,0)
        # and moves left to right on odd rows (0 based) and right to left on odd rows
        # at row end move up (subtract from y)

        #first move
        if playerX < 0:
            playerX_new = spin-1
            playerY_new = 9
        else:
            #odd row
            if playerY % 2:
                #move left to right same row
                if (playerX + spin) <= self.__boardSize-1:
                    playerX_new += spin
                #move left to right and then up a row and to the left
                else:
                    playerX_new = 2*self.__boardSize - 1 - spin - playerX
                    playerY_new -= 1
            else:
                #move right to left same row
                if (playerX - spin) >= 0:
                    playerX_new -= spin
                #move right to left and then up a row and to the right
                else:
                    playerX_new = spin - playerX - 1
                    playerY_new -= 1
        
        #check for move winning move past [0,0]
        if playerY_new < 0:
            playerY_new = playerX_new = 0

        #check for chute or ladder
        cell = self.__gameBoard[playerY_new][playerX_new][:3]
        if cell in self.__CandLmap:
            playerY_new = self.__CandLmap[cell][0]
            playerX_new = self.__CandLmap[cell][1]

        self.__player_loc[turn] = [playerY_new, playerX_new]

        # update previous spot
        if playerX >= 0:
            cellCurrent = self.__gameBoard[playerY][playerX]
            if cellCurrent[5] == str(turn):
                cellCurrentNew = cellCurrent[:5] + '-'
            else:
                cellCurrentNew = cellCurrent[:4] + '-' + cellCurrent[5]
      
            self.__gameBoard[playerY][playerX] = cellCurrentNew

        # update new spot
        cellNew = self.__gameBoard[playerY_new][playerX_new]
        if cellNew[5] == '-':
            cellNewValue = cellNew[:5] + str(turn)
        else:
            cellNewValue = cellNew[:4] + str(turn) + cellNew[5]

        self.__gameBoard[playerY_new][playerX_new] = cellNewValue
    
    # check for winner
    def checkWinner(self,turn):
        return self.__player_loc[turn] == [0][0]

    # Print out game board
    def printBoard(self):
        for row in self.__gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")

        
