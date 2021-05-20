class Contacts(object):

    def __init__(self, name,phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


    def get_contact(self):
        return f'주소록: 이름 {self.name}, 전화번호 {self.phone}, 이메일 {self.email}. 주소 {self.address}'

    @staticmethod
    def main():

            while True:
                menu = int(input("1. 주소록 추가\n0.프로그램 종료"))
                if menu == 1:
                    c = Contacts(input('이름'), input('전화번호'), input('이메일'), input('주소'))
                    print(c.get_contact())
                elif menu == 0:
                    break


Contacts.main()