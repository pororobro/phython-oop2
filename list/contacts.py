'''
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''

class Contacts(object):
    def __init__(self, name,number, email, address):
        self.name = name
        self.number = number
        self.email= email
        self.address = address

    def get_contacts(self):
        return self.name, self.number, self.email, self.address

    @staticmethod
    def main():
        c = Contacts(input('이름을 입력하세요'),int(input('전화번호를 입력하세요')),
                     input('이메일을 입력학세요'),input('주소를 입력하세요'))
        print(f'연락처:{c.get_contacts()}')

Contacts.main()
