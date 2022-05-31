from RoshamboPlayer import RoshamboPlayer


class Move:
    def __init__(self, move, score):
        self.move = move
        self.score = score


class Agent(RoshamboPlayer):
    def __init__(self):
        super().__init__()
        self.moves = []
        self.trial = 1000

    def newGame(self, trial):
        self.moves = []
        self.trial = trial

    def storeMove(self, move, score):
        self.moves.append(Move(move, score))

    def nextMove(self):
        pass

    def getName(self):
        return "My Agent"

    def getAuthor(self):
        return "MORSY & SAMER"
