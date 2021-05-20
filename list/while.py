class Practice(object):
    def __init__(self):
        pass

    @staticmethod
    def main():
        while 1:
            menu = int(input('1 입력 시 진행\n0 입력 시 스탑'))
            if menu == 1:
                food = input('1.햄버거, 2.피자, 3.치킨')
                if food == 1:
                    print('햄버거를 주문하셨습니다')
                elif food == 2:
                    print('피자를 주문하셨습니다')
                elif food == 3:
                    print('치킨을 주문하셨습니다')
                else :
                    print('잘못 누르셨습니다')
                    break
            if menu == 0:
                break

Practice.main()

