import random
class Account(object):
    def __init__(self, customer, balance):
        self.customer = customer
        self.balance = balance
        self.BANK_NAME = 'SC은행'  # 상수는 대문자로 선언한다.
        self.acc_number = self.create_acc_number(3)
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''
    def create_acc_number(self, count):  # 아직 오류 발생중
        a = ''
        for i in range(count):
             ran = random.randint(0, 9)
        print(f's의 랜덤값은 {a}')

    def to_string(self):
        return f'<생성된 계좌정보>\n 은행이름: {self.BANK_NAME}\n 계좌번호: {self.acc_number}\n' \
               f'예금주: {self.customer}, 초기잔액: {self.balance}'
    @staticmethod
    def del_element(account_lists, customer):
        for i, j in enumerate(account_lists):
            if j.customer == customer:
                del account_lists[i]
    @staticmethod
    def main():
        account_lists = []
        while True:
            select = input('0. 종료\n 1. 입력\n 2. 출력\n 3.수정\n 4.삭제\n ')
            if select == '0':
                account = Account(None, None)
                print(account.create_acc_number(3))
                # print('프로그램 종료됩니다')
                break
            elif select == '1':
                account_lists.append(Account(input('예금주를 입력하세요'), input('초기잔액을 입력하세요')))
            elif select == '2':
                for i in account_lists:
                    print(i.to_string())
            elif select == '3':
                customer = input('성함을 입력해주세요')
                account = Account(customer, input('초기잔액을 입력하세요'))
                account.del_element(account_lists, customer)
                account_lists.append(account)
            elif select == '4':
                account = Account(input('예금주를 입력하세요'), None)
                account.del_element(account_lists, account.customer)
                print('삭제가 완료되었습니다.')
            else:
                print('다시입력하세요')
                continue
Account.main()