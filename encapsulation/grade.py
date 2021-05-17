class Grade:
    def setgrade(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math

    def sum(self):
        return self.korean+self.english+self.math

    def avg(self):
        return self.sum() / 3


if __name__ == '__main__':
    g = Grade()
    g.setgrade(95,96,90)
    print(g.sum())
    print(g.avg())


