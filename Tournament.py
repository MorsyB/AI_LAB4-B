from Dummies import *


class Tournament:
    def __init__(self):
        self.participants = []
        self.addPlayers()

    def addPlayers(self):
        self.participants(AntiFlat())
        self.participants(Copy())
        self.participants(Freq())
        self.participants(Flat())
        self.participants(Foxtrot())
        self.participants(Bruijn81())
        self.participants(Pi())
        self.participants(Play226())
        self.participants(RndPlayer())
        self.participants(Rotate())
        self.participants(Switch())
        self.participants(SwitchALot())
