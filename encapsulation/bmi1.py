#def Bmi(weight,height):
 #     return weight / height ** 2 * 10000




class Bmi(object):

        def __init__(self, height, weight):
            self.height = height
            self.weight = weight

        def getBmi(self):
            bmi = ''
            index = self.weight / self.height ** 2 * 10000
            if index >= 35:
                bmi = '고도 비만'
            elif index >= 30:
                bmi = '중도 비만'
            elif index >= 25:
                bmi = '경도 비만'
            if index >= 23:
                bmi = '과체중'
            if index >= 18.5:
                bmi = '정상'
            else:
                bmi = '저체중'
            return bmi

        @staticmethod
        def main():
            b = Bmi(int(input('키(cm)')),int(input('몸무게(kg)')))
            print(f'당신의 BMI는 {b.getBmi()}입니다')


#if __name__ == '__main__':
    #b = Bmi(180,70)
    #print(b.getBmi())
Bmi.main()