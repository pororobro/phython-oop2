

import random

class Account(object):
    def __init__(self, holder,account_number, balance):
        self.bank = 'SC제일은행'
        self.holder = holder
        self.balance = balance
        self.account_number = account_number


    def get_account(self):

        return f'은행이름:{self.bank} 예금주:{self.holder} 계좌번호:{self.account_number} 잔액:{self.balance}'

    @staticmethod
    def random_number():
        first = random.randint(0, 999)
        second = random.randint(0, 99)
        third = random.randint(0, 999999)

        first = str(first).zfill(3)
        second = str(second).zfill(2)
        third = str(third).zfill(6)

        return first + '-' + second + '-' + third

    @staticmethod
    def main():

        account_howmany = 0
        ls = []
        while 1:
            menu = input('0.취소 1.계좌생성 2.확인 3.제거')

            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('예금주를 입력해주세요'),Account.random_number(),int(input('초기잔액을 입력해주세요'))))
                account_howmany+=1
                print(f'생성 계좌 수: {account_howmany}')

            elif menu == '2':
                for i in ls:
                    print(i.get_account())

            elif menu == '3':
                del_number = input('제거 할 계좌번호: ')
                for i, j in enumerate(ls):
                    if j.account_number == del_number:
                        del ls[i]

            else:
                print('잘못된 입력입니다')
                continue
Account.main()





