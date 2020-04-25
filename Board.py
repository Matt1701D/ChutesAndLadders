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
        self.__initCandLmap(["CT1",0,2], ["CB1",2,2])
        self.__initCandLmap(["CT2",0,5], ["CB2",2,5])
        self.__initCandLmap(["CT3",0,7], ["CB3",2,7])
        self.__initCandLmap(["CT4",3,1], ["CB4",8,1])
        self.__initCandLmap(["CT5",3,3], ["CB5",4,0])
        self.__initCandLmap(["CT6",4,4], ["CB6",4,7])
        self.__initCandLmap(["CT7",5,7], ["CB7",7,5])
        self.__initCandLmap(["CT8",5,8], ["CB8",8,9])
        self.__initCandLmap(["CT9",8,4], ["CB9",9,5])
        self.__initCandLmap(["CT0",1,6], ["CB0",7,3])

        #insert ladders
        self.__initCandLmap(["LB1",2,0], ["LT1",0,0])
        self.__initCandLmap(["LB2",7,7], ["LT2",1,3])
        self.__initCandLmap(["LB3",2,9], ["LT3",0,9])
        self.__initCandLmap(["LB4",4,9], ["LT4",3,6])
        self.__initCandLmap(["LB5",7,0], ["LT5",5,1])
        self.__initCandLmap(["LB6",6,4], ["LT6",5,3])
        self.__initCandLmap(["LB7",9,0], ["LT7",6,2])
        self.__initCandLmap(["LB8",9,8], ["LT8",6,9])
        self.__initCandLmap(["LB9",9,3], ["LT9",8,6])
    
    # initalize chutes and ladder locations
    def __initCandLmap(self, key, value):

        y = key[1]
        x = key[2]
        self.__gameBoard[y][x] = key[0]+'---'

        y = value[1]
        x = value[2]
        self.__gameBoard[y][x] = value[0]+'---'

        self.__CandLmap[key[0]] = [y,x]

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
            playerY_new = self.__boardSize-1
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
        
        #check for winning move past [0,0]
        if playerY_new < 0:
            playerY_new = playerX_new = 0

        #check for chute or ladder
        cell = self.__gameBoard[playerY_new][playerX_new][:3]
        if cell in self.__CandLmap:
            playerY_new = self.__CandLmap[cell][0]
            playerX_new = self.__CandLmap[cell][1]

        # update previous spot on gameboard
        if playerX >= 0:
            cellCurrent = self.__gameBoard[playerY][playerX]
            if cellCurrent[5] == str(turn):
                cellCurrentNew = cellCurrent[:5] + '-'
            else:
                cellCurrentNew = cellCurrent[:4] + '-' + cellCurrent[5]
      
            self.__gameBoard[playerY][playerX] = cellCurrentNew

        # update new spot on gameboard
        cellNew = self.__gameBoard[playerY_new][playerX_new]
        if cellNew[5] == '-':
            cellNewValue = cellNew[:5] + str(turn)
        else:
            cellNewValue = cellNew[:4] + str(turn) + cellNew[5]

        self.__gameBoard[playerY_new][playerX_new] = cellNewValue
        
        # update player location
        self.__player_loc[turn] = [playerY_new, playerX_new]
    
    # check for winner
    def checkWinner(self,turn):
        return self.__player_loc[turn] == [0,0]

    # Print out game board
    def printBoard(self):
        for row in self.__gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")

        
