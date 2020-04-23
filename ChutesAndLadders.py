import random, Board

class ChutesAndLadders:

    #initialize game
    def __init__(self):
        self.playerNum = 2
        self.maxspin = 6
        self.board = Board.Board(10, self.playerNum)
        self.players = self.getPlayers()
        
        self.turn = 0
        self.playGame()

    def getPlayers(self):
        print("Welcome to Chutes and Ladders")

        players = []
        while(len(players) < self.playerNum):
            player = input("Enter unique name for player " + str(len(players)+1) + ": ")
            if not player in players:
                players.append(player)
        
        return players

    def playGame(self):
        while(1):
            input(self.players[self.turn] + " press Enter to spin")
            print("\n")

            spin = random.randint(1,self.maxspin)
            print("You spun a " + str(spin))

            self.board.makeMove(self.turn, spin)
            print("\n")
            self.board.printBoard()

            self.turn ^= 1

if __name__ == '__main__':
    myCandL = ChutesAndLadders()
