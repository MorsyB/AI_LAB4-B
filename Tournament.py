from Dummies import *
from Agent import *
from random import uniform

class Tournament:
    def __init__(self):
        self.maxIter = 1000
        self.participants = []
        self.score = []
        self.population=[]
        self.buffer=[]
        self.popsize=2048
        self.addPlayers()
        self.matchHistory = []
        self.start()
        self.init_population()
        #print(self.score)



    def init_population(self):
        for i in range(self.popsize):
            Citizen= Agent()
            self.population.append(Citizen)
            self.buffer.append(Citizen)

    def Agents_game(self):
        for i in range(self.popsize):
            finalscore=0
            for player in range(len(self.participants)):
                finalscore+= self.startGame2(self.population[i],player)
            self.population[i].score = finalscore
            #print(finalscore)


    def calc_fitness(self):
        for i in range(self.popsize):
            self.population[i].fitness= self.population[i].score
            self.population[i].score=0

    def addPlayers(self):
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

    def startGame2(self, player1, player2):
        self.participants[player2].newGame(1000)
        score1, score2 = 0, 0
        for i in range(1000):
            move1 = player1.moves[i]
            move2 = self.participants[player2].nextMove()
            if (move1 == 0 and move2 == 1) or (move1 == 1 and move2 == 2) or (move1 == 2 and move2 == 0):
                score2 += 1
                score1 -= 1
                self.participants[player2].storeMove(move2, 1)

            elif (move2 == 0 and move1 == 1) or (move2 == 1 and move1 == 2) or (move2 == 2 and move1 == 0):
                score1 += 1
                score2 -= 1

                self.participants[player2].storeMove(move2, -1)
            else:
                self.participants[player2].storeMove(move2, 0)

        self.score[player2] += score2
        if score2 > score1:
            return -1

        return 1


    def startGame(self, player1, player2):
        self.participants[player1].newGame(1000)
        self.participants[player2].newGame(1000)
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

    def mutualism_phase(self,best):
        for i in range(self.popsize):
            index=randint(0,self.popsize)
            while index==i:
                index=randint(0,self.popsize)
            BF1= randint(1,2)
            BF2= randint(1,2)
            mutual_vector= (self.population[i].moves+self.population[index].moves)/2
            newvec1= self.population[i].moves+ uniform(0,1)*(best.moves-mutual_vector*BF1)
            newvec2 = self.population[index].moves + uniform(0,1) * (best.moves - mutual_vector * BF2)



    def run(self):
        best=self.population[0]
        for i in range(self.maxIter):
            self.Agents_game()
            self.calc_fitness()
            self.sort_by_fitness()
            if self.population[0].fitness >best.fitness:
                best=self.population[0]
            self.mutualism_phase(best)
            self.Commensalism_phase()
            self.paratisim_phase()


