class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def to_string(self):
        return f'종목명 {self.name}, 종목코드 {self.code}'

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('o.Exit 1.Create 2.Read 3.Update 4.Delete')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input('name'),input('code')))
            elif menu == '2':
                for i in ls:
                    print(i)
            elif menu == '3':
                edit_code = input('수정할 종목코드')
                stock = Stock(input('수정할 이름'), edit_code)
                for i, j in enumerate(ls):
                    if j.code == edit_code:
                        del ls[i]
                        ls.append(stock)

            elif menu == '4':
                del_name =input('삭제할 종목명')
                for i in enumerate(ls):
                    if j.name == del_name:
                        del [i]
            else :
                print('Wrong number')
                continue

Stock.main()
