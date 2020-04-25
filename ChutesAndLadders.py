import random, Board

class ChutesAndLadders(object):

    #initialize game
    def __init__(self):
        self.playerNum = 3
        self.maxSpin = 6 #has to be at most equal to boardSize
        self.boardSize = 10
        self.board = Board.Board(self.boardSize, self.playerNum)
        self.players = self.getPlayers()
        self.turn = 0

        self.playGame()

    #get player names
    def getPlayers(self):
        print("Welcome to Chutes and Ladders")

        players = []
        while(len(players) < self.playerNum):
            player = input("Enter unique name for player " + str(len(players)+1) + ": ")
            if not player in players:
                players.append(player)
        
        return players

    #have players spin and move
    def playGame(self):
        gameWon = 0
        while(not(gameWon)):
            input(self.players[self.turn] + " press Enter to spin")
            print("\n")

            spin = random.randint(1,self.maxSpin)
            print("You spun a " + str(spin))

            self.board.makeMove(self.turn, spin)
            print("\n")
            self.board.printBoard()

            gameWon = self.board.checkWinner(self.turn)
            if gameWon:
                print("\n")
                print(self.players[self.turn] + " wins!")
            else:
                self.turn = 0 if self.turn+1 > self.playerNum-1 else self.turn+1

if __name__ == '__main__':
    myCandL = ChutesAndLadders()
