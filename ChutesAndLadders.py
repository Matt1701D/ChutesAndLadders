import Board

class ChutesAndLadders:

    #initialize game
    def __init__(self):
        self.board = Board.Board(10)
        self.playernum = 2
        self.players = self.getPlayers()
        
        self.turn = 1
        self.playGame()

    def getPlayers(self):
        print("Welcome to Chutes and Ladders")

        players = set()
        while(len(players) < self.playernum):
            player = input("Enter unique name for player " + str(len(players)+1) + ": ")
            if not player in players:
                players.add(player)
        
        return players

    def playGame(self):
        print(self.players)
        self.board.printBoard()

if __name__ == '__main__':
    myCandL = ChutesAndLadders()
