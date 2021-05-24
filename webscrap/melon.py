from bs4 import BeautifulSoup
from urllib.request import urlopen

class BugsMusic(object):
     url = ''

    def __str__(self): #이 안에 들어있는
        return self.url

    @staticmethod
    def main():
        bugs = BugsMusic()
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Print URL'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input URL')
            elif menu == 2:
                print(f':입력된 URL :::::::::::::::::::: {bugs.url}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')

                count = 0
                for link1 in soup.find_all(name='div', attrs=({"class": "ellipsis rank01"})):
                    count += 1
                    print(f'{str(count)} RANKING')
                    print(f'TITLE: {link1.find("a").text}')

            else:
                print('Wrong number')
                continue



BugsMusic.main()
