class TreasureChest:
    # PRIVATE question : STRING
    # PRIVATE answer, points : INTEGER

    def __init__(self, questionP, answerP, pointsP):
        self.question = questionP
        self.answer = answerP
        self.points = pointsP

    def getQuestion(self):
        return self.question

    def checkAnswer(self, UserAnswer):

        if UserAnswer == self.answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.points)
        elif attempts == 2:
            temp = self.points // 2
            return int(temp)
        elif attempts == 3 or attempts == 4:
            temp = self.points // 4
            return temp
        else:
            return 0
