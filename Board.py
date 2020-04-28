class Board(object):

    def __init__(self, boardSize, playerNum):
        self.__boardSize = boardSize
        self.__playerNum = playerNum
        self.__gameBoard = []
        self.__CandLmap = {}
        self.__player_loc = {}
        self.__delimeter = '-'

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
        cellLength = 4 + self.__playerNum
        self.__gameBoard = [[self.__delimeter*cellLength] * self.__boardSize for x in range(self.__boardSize)]

        # set players off the board
        for i in range(self.__playerNum):
            self.__player_loc[i] = 0
        
        self.__CandLmap = {1:38, 4:14, 9:31, 16:6, 21:42, 28:84, 36:44,
                            48:26, 49:11, 51:67, 56:53, 62:19, 64:60,
                            71:91, 80:100, 87:24, 93:73, 95:75, 98:78}

        # make Chutes and Ladder labels and place on board
        ladderCount = chuteCount = 0
        delimString = self.__delimeter*(cellLength-3)
        for item in self.__CandLmap:
            key = item
            value = self.__CandLmap[item]

            if key > value:
                labelKey = 'CT'+str(chuteCount)+delimString
                labelValue = 'CB'+str(chuteCount)+delimString
                chuteCount += 1
            else:
                labelKey = 'LB'+str(ladderCount)+delimString
                labelValue = 'LT'+str(ladderCount)+delimString
                ladderCount += 1
        
            self.__placeOnBoard(key, labelKey)
            self.__placeOnBoard(value, labelValue)

    # convert position into grid coordinates and update gameBoard
    def __placeOnBoard(self,position,turn,isNewPos=False):
        label = turn
        gridCoord = self.__posToGrid(position)
        y = gridCoord[0]
        x = gridCoord[1]

        # if updating previous player position, look for player number to replace, 
        # else for new player position replace right most '-' with player number
        if str(turn).isnumeric():
            if isNewPos:
                delimeter = self.__delimeter
            else:
                delimeter = str(turn)
                label = self.__delimeter

            labelCur = self.__gameBoard[y][x]

            playerFound = False
            cellLength = 4 + self.__playerNum
            while(not(playerFound)):
                if labelCur[cellLength-1] == delimeter:
                    label = labelCur[:cellLength-1] + str(label) + labelCur[cellLength:]
                    playerFound = True
                #elif labelCur[5] == delimeter:
                    #label = labelCur[:5] + str(label) + labelCur[6]
                else:
                    #label = labelCur[:4] + str(label) + labelCur[5] + labelCur[6]
                    cellLength-=1
            
        self.__gameBoard[y][x] = label

    # convert position into grid coordinates and update gameBoard
    def __posToGrid(self,position):
        # convert position to grid coordinates (remember board starts at (9,0), moves Left to Right and Up
        # and then Right to Left and Up
        y = self.__boardSize - 1 - int((position-1) / self.__boardSize)
        x = (position-1) % self.__boardSize if y%2 else self.__boardSize - 1 - ((position-1) % self.__boardSize)

        return [y, x]

    # PUBLIC METHODS

    # Compute the location for current move and move player
    def makeMove(self, turn, spin):
        # get player pos
        pos_current = self.__player_loc[turn]
        pos_new = 100 if pos_current + spin > 100 else pos_current + spin

        # check for chute or ladder
        pos_new = self.__CandLmap.get(pos_new,pos_new)

        # remove old player location
        if pos_current > 0:
            self.__placeOnBoard(pos_current, turn, False)
        
        # update player location
        self.__player_loc[turn] = pos_new
        self.__placeOnBoard(pos_new, turn, True)
    
    # check for winner
    def checkWinner(self,turn):
        return self.__player_loc[turn] == 100

    # Print out game board
    def printBoard(self):
        for row in self.__gameBoard:
            print(' '.join([str(s) for s in row]))
        print("\n")

        
