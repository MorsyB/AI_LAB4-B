import time
from Greenberg import *
from RoshamboPlayer import RoshamboPlayer
from iocaine import iocaine_agent


class Urza(RoshamboPlayer):
    def __init__(self):
        pass

    def newGame(self, trial):
        pass

    def storeMove(self, move, score):
        pass

    def nextMove(self):
        pass

    def getName(self):
        pass

    def getAuthor(self):
        pass


class megaHal(RoshamboPlayer):
    def __init__(self):
        pass

    def newGame(self, trial):
        pass

    def storeMove(self, move, score):
        pass

    def nextMove(self):
        pass

    def getName(self):
        pass

    def getAuthor(self):
        pass


class Observation:
    def __init__(self):
        self.step = 0
        self.lastOpponentAction = 0


class Iocaine(RoshamboPlayer):
    def __init__(self):
        super().__init__()
        self.observe = Observation()

    def newGame(self, trial):
        self.observe = Observation()

    def storeMove(self, move, score):
        self.observe.step += 1
        self.observe.lastOpponentAction = move

    def nextMove(self):
        return iocaine_agent(self.observe, 0)

    def getName(self):
        return "iocaine"

    def getAuthor(self):
        return "Robby"


class Greenberg(RoshamboPlayer):
    def __init__(self):
        super().__init__()
        self.opp_moves = []
        self.moves = 0

    def newGame(self, trial):
        self.opp_moves = []
        self.moves = 0

    def storeMove(self, move, score):
        self.moves += 1

    def nextMove(self):
        return player(self.moves, self.opp_moves)

    def getName(self):
        return "Greenberg"

    def getAuthor(self):
        return "Samer El\"GAY\""
