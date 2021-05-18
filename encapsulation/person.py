'''
이름, 출생년도 ,주소를 입력받아서
회원가입한 사람의 이름, 나이, 주소를 출력하시오
'''

class Person(object):
    def __init__(self, name, year,month, address):
        self.name = name
        self.year = year
        self.month = month
        self.address = address

    def myage(self):
        age = ''
        age = 2021- self.year -1
        mon = self.month
        if mon < 5:
            age+=1
        else:
            age

        return age

    @staticmethod
    def main():
        p = Person(input('이름'),int(input('출생(년도)')),int(input('출생(월)')),input('주소'))
        print(f'이름:{p.name}')
        print(f'나이:{p.myage()}')
        print(f'주소:{p.address}')

Person.main()




