class Bmi:
    def setbmidata(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / self.height ** 2 * 10000

if __name__ == '__main__':
    b = Bmi()
    b.setbmidata(180, 70)
    print(b.bmi())