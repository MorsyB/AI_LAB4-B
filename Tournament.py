from Dummies import *
from Agent import *


class Tournament:
    def __init__(self):
        self.participants = []
        self.score = []
        self.addPlayers()
        self.matchHistory = []

    def addPlayers(self):
        self.participants.append(Agent())
        self.participants.append(AntiFlat())
        self.participants.append(Copy())
        self.participants.append(Freq())
        self.participants.append(Flat())
        self.participants.append(Foxtrot())
        self.participants.append(Bruijn81())
        self.participants.append(Pi())
        self.participants.append(Play226())
        self.participants.append(RndPlayer())
        self.participants.append(Rotate())
        self.participants.append(Switch())
        self.participants.append(SwitchALot())
        for _ in range(len(self.participants)):
            self.score.append(0)

    def start(self):
        for player1 in range(len(self.participants) - 1):
            player1History = []
            for player2 in range(player1 + 1, len(self.participants)):
                finalScore = self.startGame(player1, player2)
                player1History.append(finalScore)
            self.matchHistory.append(player1History)

    def startGame(self, player1, player2):
        score1, score2 = 0, 0
        for _ in range(1000):
            move1 = self.participants[player1].nextMove()
            move2 = self.participants[player2].nextMove()
            if (move1 == 0 and move2 == 1) or (move1 == 1 and move2 == 2) or (move1 == 2 and move2 == 0):
                score2 += 1
                score1 -= 1
                self.participants[player2].storeMove(move2, 1)
                self.participants[player1].storeMove(move1, -1)

            elif (move2 == 0 and move1 == 1) or (move2 == 1 and move1 == 2) or (move2 == 2 and move1 == 0):
                score1 += 1
                score2 -= 1
                self.participants[player1].storeMove(move1, 1)
                self.participants[player2].storeMove(move2, -1)
            else:
                self.participants[player1].storeMove(move1, 0)
                self.participants[player2].storeMove(move2, 0)

        self.score[player1] += score1
        self.score[player2] += score2

        if score2 > score1:
            return -1
        return 1
