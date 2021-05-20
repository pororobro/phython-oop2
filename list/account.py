#import random
#random

class Account(object):
    def __init__(self, holder, number, balance):
        self.bank = 'sc 제일은행'
        self.holder = holder
        self.number = number
        self.balance = balance

    def get_acount(self):

        return f'은행:{self.bank} 예금주:{self.holder} 계좌번호:{self.number} 잔액:{self.balance}'



    @staticmethod
    def main():
        while 1:
            menu = input('0.취소 1.계좌생성 2.확인')
            if menu == '0':
                break
            elif menu == '1':
                a = Account(input('예금주를 입력해주세요'),int(input('초기잔액을 입력해주세요')))
            elif menu == '2':
                print(a.get_acount())
            else:
                print('잘못된 입력입니다')

Account.main()





