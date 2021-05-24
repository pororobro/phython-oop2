from bs4 import BeautifulSoup
from urllib.request import urlopen


class BugsMusic(object):

    url = ''

    def __str__(self): #이 안에 들어있는
        return self.url

    #https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210524&charthour=15
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

                print('------------------------- ARTIST RANKING ---------------------------')
                n_artist = 0
                for link1 in soup.find_all(name='p', attrs=({"class":"artist"})):
                    n_artist += 1
                    print(f'{str(n_artist)} RANKING')
                    print(f'TITLE: {link1.find("a").text}')

                print('------------------------- TITLE RANKING ---------------------------')
                n_title = 0
                for link1 in soup.find_all(name='p', attrs=({"class":"title"})):
                    n_title += 1
                    print(f'{str(n_title)} RANKING')
                    print(f'TITLE: {link1.find("a").text}')

            else:
                print('Wrong number')
                continue



BugsMusic.main()