import Board

class ChutesAndLadders:

    #initialize game
    def __init__(self):
        self.playerNum = 2
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
        input(self.players[self.turn] + " press a key to spin")
        print("\n")
        self.board.makeMove(self.turn)
        print("\n")
        self.board.printBoard()

if __name__ == '__main__':
    myCandL = ChutesAndLadders()
