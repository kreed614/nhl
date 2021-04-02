from misc_functions import Misc_Functions

from bs4 import BeautifulSoup
import time


class Starting_Goalies:
    def __init__(self):
        self.mf = Misc_Functions()

    def get_starting_goalies(self):
        html = self.mf.get_page_source(
            'https://www.dailyfaceoff.com/starting-goalies/', 3)
        soup = BeautifulSoup(html, 'html.parser')

        card = soup.find('div', class_='starting-goalies-list stat-cards-list')

        names = card.find_all('h4')
        temp_matchups = []
        n = 0
        # strength = card.find_all('h5', class_='news-strength not-confirmed')
        # for news in strength:
        #     print(news.get_text())

        for __ in range(len(names)//3):
            temp = []
            for __ in range(3):
                if names[n].get_text() == 'Cal Petersen':
                    temp.append('Calvin Petersen')
                else:
                    temp.append(names[n].get_text())
                n += 1
            temp_matchups.append(temp)
        matchups = {}
        for matchup in temp_matchups:
            matchups[matchup[0]] = {}
            matchups[matchup[0]] = [
                f'{matchup[1][0]}.{matchup[1]}', f'{matchup[2][0]}.{matchup[2]}']

        return matchups
