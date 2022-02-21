import random
from hangman.GameImpl import GameImpl
from hangman.FileIO import FileIO

class Hangman(GameImpl):
    def __init__(self, fileIO: FileIO):
        self.fileIO = fileIO
        self.array = self.fileIO.openFile("test.txt")
        self.rankList = self.fileIO.openFile("rank.txt")
        self.userName = self.answer = ""
        self.trialCnt = self.score = 0
        self.maxTrialCnt = 10
        self.checkList = []
        self.isCorrect = False


    def getUserName(self):
        self.userName = input("Enter your name(Numbers are not allowed): ")
        float(self.userName)
    

    def execute(self):
        while True:
            self.chooseWord()

            while self.trialCnt < self.maxTrialCnt and not self.isCorrect:
                self.getUserGuess()

            self.score += self.maxTrialCnt - self.trialCnt
            self.printResult()
            if not self.goAgain():
                break

        self.updateRankList()
        self.showRankList(5)


    def chooseWord(self):
        self.answer = random.choice(self.array)
        self.checkList = ['_' for _ in range(len(self.answer))]
        self.trialCnt = 0
        self.isCorrect = False


    def getUserGuess(self):
        print(self.userName + ", guess the word or its character(", end="")
        print(str(self.trialCnt) + "/" + str(self.maxTrialCnt) + ")!")
        print(self.checkList)
        guess = input("Enter: ")

        if len(guess) > 1:
            self.checkWord(guess) 
        else:
            self.checkChar(guess)

        if '_' not in self.checkList:
            self.isCorrect = True


    def checkWord(self, guess):
        if guess == self.answer:
            self.isCorrect = True
        else:
            self.trialCnt += 1


    def checkChar(self, guess):
        hasChangedOnce = False
        for i, c in enumerate(self.answer):
            if guess == c:
                self.checkList[i] = c
                hasChangedOnce = True
        if hasChangedOnce:
            hasChangedOnce = False
        else:
            self.trialCnt += 1


    def printResult(self):
        if self.isCorrect:
            print(self.userName + ", you got the answer(" + self.answer + ").")
        else:
            print("Maybe next time!")


    def goAgain(self):
        while True:
            ans = input(self.userName + ", try again(Y/N)? ")
            if ans == 'Y' or ans == 'y':
                return True
            if ans == 'N' or ans == 'n':
                return False

    
    def updateRankList(self):
        self.updateUserScore()
        self.sortRankList()
        self.fileIO.saveFile("rank.txt", self.rankList)


    def updateUserScore(self):
        for i, line in enumerate(self.rankList):
            if self.userName in line:
                self.score += int(line.split(',')[1])
                self.rankList[i] = self.userName + "," + str(self.score)
                return True

        self.rankList.append(self.userName + "," + str(self.score))


    def sortRankList(self):
        tmpTuples = self.convertStringToTuple(self.rankList)
        tmpTuples = sorted(tmpTuples, key=lambda score:score[1], reverse=True)
        for i, tuple in enumerate(tmpTuples):
            self.rankList[i] = tuple[0] + ',' + str(tuple[1])


    def convertStringToTuple(self, list):
        tmpTuples = []
        for line in list:
            tmpTuple = (line.split(',')[0], int(line.split(',')[1]))
            tmpTuples.append(tmpTuple)
        return tmpTuples

    def showRankList(self, maxLineNum):
        for i, line in enumerate(self.rankList):
            if i == maxLineNum:
                break
            print(str(i + 1) + ". " + line)
