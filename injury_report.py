from misc_functions import Misc_Functions
from bs4 import BeautifulSoup


class Injury_Report():
    def get_injuries(self):

        mf = Misc_Functions()

        url = "https://www.espn.com/nhl/injuries"

        soup = BeautifulSoup(mf.get_page_source(url, 1), 'html.parser')
        card = soup.find('div', class_="page-container cf")

        teams = card.find_all('span', class_="injuries__teamName ml2")
        players = card.find_all('tbody', class_="Table__TBODY")
        injured = []
        for player in players:
            stats = player.find_all('tr')
            for tr in stats:
                name = tr.find('a').get_text().split('  ')
                try:
                    name = f'{name[0][0]}.{name[0]} {name[1]}'
                except IndexError:
                    continue
                injured.append(name)

        return injured
