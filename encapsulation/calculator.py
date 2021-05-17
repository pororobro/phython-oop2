def test():
    pass

class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second

if __name__ == '__main__':
    c = Calculator()
    c.setdata(1,2)
    print(c.second + c.first)
    print(c.second - c.first)
    print(c.second * c.first)
    print(c.second / c.first)
    print(c.second % c.first)


