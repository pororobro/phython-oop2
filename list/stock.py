class Stock(object):
    def __init__(self, ticker, code ):
        self.ticker = ticker
        self.code = code

    def stockdata(self):
        return f'종목명은 {self.ticker}이며 종목코드는 {self.code}입니다'

    @staticmethod
    def main():
        while 1:
            menu = input('0.취소 1.입력 2.출력')
            if menu == '0':
                break
            elif menu == '1':
                s = Stock(input('종목명을 입력해주세요'),input('종목코드를 입력해주세요'))
            elif menu == '2':
                print(f'입력하신 {s.stockdata()}')
                break

Stock.main()