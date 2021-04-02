from misc_functions import Misc_Functions

from bs4 import BeautifulSoup
import requests
import time


class Player_Stats():
    def __init__(self):
        self.mf = Misc_Functions()

    def html_to_text(self, html_text):
        result = []
        temp_res = []
        for line in html_text:
            line = line.get_text().split('\n')
            for element in line:
                if element:
                    temp_res.append(element)
            temp_res[0] = temp_res[0].lstrip()
            result.append(temp_res)
            temp_res = []
        return result

    def format_player(self, player, ptype):
        player_dict = {}
        if ptype == 'goalie':
            player_dict['player'] = player[0]
            player_dict['gp'] = player[1]
            player_dict['gs'] = player[2]
            player_dict['w'] = player[3]
            player_dict['l'] = player[4]
            player_dict['t'] = player[5]
            player_dict['ot'] = player[6]
            player_dict['sa'] = player[7]
            player_dict['ga'] = player[8]
            player_dict['gaa'] = player[9]
            player_dict['s'] = player[10]
            player_dict['sv%'] = player[11]
            player_dict['so'] = player[12]
            player_dict['min'] = player[13]

        elif ptype == 'skater':
            player_dict['player'] = player[0]
            player_dict['gp'] = player[1]
            player_dict['g'] = player[2]
            player_dict['a'] = player[3]
            player_dict['p'] = player[4]
            player_dict['+/-'] = player[5]
            player_dict['pim'] = player[6]
            player_dict['ppg'] = player[7]
            player_dict['ppp'] = player[8]
            # smg is a typo for shg
            player_dict['smg'] = player[9]
            player_dict['shp'] = player[10]
            player_dict['gwg'] = player[11]
            player_dict['otg'] = player[12]
            player_dict['s'] = player[13]
            player_dict['s%'] = player[14]
            player_dict['fo%'] = player[15]

        return player_dict

    def get_data(self, team_names):
        nhl_stats = {}
        nhl_stats['goalies'] = {}
        nhl_stats['skaters'] = {}
        nhl_stats['teams'] = {}

        for team in team_names:
            url = f'https://www.nhl.com/{team}/stats/regular-season'
            html = self.mf.get_page_source(url, 2)
            soup = BeautifulSoup(html, 'html.parser')

            team_title = soup.find('title')
            try:
                team_name = team_title.get_text().split('|')[2].strip()
                print(f"{team_name}, complete")
            except IndexError as i:
                print(f"{team}: {i}")
                continue
            nhl_stats['teams'][team_name] = {}

            # Goalies
            goalie_div = soup.find('div', id='goalie-table')
            goalies = goalie_div.find_next('tbody').find_all('tr')

            # Skaters
            skater_div = soup.find('div', id='skater-table')
            skaters = skater_div.find_next('tbody').find_all('tr')

            skaters = self.html_to_text(skaters)
            goalies = self.html_to_text(goalies)

            for goalie in goalies:
                goalie_dict = self.format_player(goalie, 'goalie')
                nhl_stats['goalies'][goalie[0]] = goalie_dict

                team_goalie_dict = self.format_player(goalie, 'goalie')
                nhl_stats['teams'][team_name][goalie[0]] = team_goalie_dict

            for skater in skaters:
                skater_dict = self.format_player(skater, 'skater')
                nhl_stats['skaters'][skater[0]] = skater_dict

                team_skater_dict = self.format_player(skater, 'skater')
                nhl_stats['teams'][team_name][skater[0]] = team_skater_dict

        return nhl_stats

    def write_daily_data(self):
        all_teams = ['ducks', 'coyotes', 'canucks', 'bruins', 'predators', 'blues',
                     'flames', 'sabres', 'hurricanes', 'blackhawks', 'avalanche', 'stars',
                     'redwings', 'oilers', 'panthers', 'kings', 'wild', 'canadiens', 'devils',
                     'islanders', 'rangers', 'senators', 'flyers', 'penguins', 'sharks', 'bluejackets',
                     'lightning', 'mapleleafs', 'goldenknights', 'capitals', 'jets']
        stats = self.get_data(all_teams)
        self.mf.write_data(stats, "perm")
