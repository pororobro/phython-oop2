

import random

class Account(object):
    def __init__(self, holder, balance):
        self.bank = 'SC제일은행'
        self.holder = holder
        self.balance = balance


    def get_account(self):

        return f'은행이름:{self.bank} 예금주:{self.holder} 계좌번호:{self.random_number()} 잔액:{self.balance}'

    def random_number(self):
        first = random.randint(0, 999)
        second = random.randint(0, 99)
        third = random.randint(0, 999999)

        first = str(first).zfill(3)
        second = str(second).zfill(2)
        third = str(third).zfill(6)

        return first + '-' + second + '-' + third

    def deposit(self):
        amount = ''
        if amount >= 1:
            self.balance += amount
        return


    @staticmethod
    def main():

        account_number = 0
        while 1:
            menu = input('0.취소 1.계좌생성 2.확인 3.입금')

            if menu == '0':
                break
            elif menu == '1':
               a = Account(input('예금주를 입력해주세요'),int(input('초기잔액을 입력해주세요')))
               account_number+=1
               print(f'생성 계좌 수: {account_number}')

            elif menu == '2':
               print(a.get_account())

            elif menu == '3':
                deposit = input('입금할 금액')
                print(a.deposit())

            else:
                print('잘못된 입력입니다')
                continue
Account.main()





