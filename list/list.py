class Contact(object):
    def __init__(self,name, phone, email, address ):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'주소록 - 이름: {self.name}, 번호: {self.phone}, 이메일: {self.email}, 주소:{self.address}'


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.Exit 1.입력 2.출력 3.삭제')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Contact(input('이름'), int(input('번호')), input('이메일'), input('주소')))
            elif menu == '2':
                for i in ls:
                    print(f'출력결과: {i.get_contact()}')
            elif menu == '3':
                    del_name = input('삭제할 이름: ')
                    for i, j in enumerate(ls):
                        if j.name == del_name:
                            del ls[i]

            else:
                print('잘못된 주문입니다')
                continue

Contact.main()
