import json
import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Misc_Functions:
    def __init__(self):
        with open('./starting_goalies.json') as f:
            self.starting_goalies = json.load(f)
        with open(f'./injuries.json') as f:
            self.injuries_data = json.load(f)
        try:
            with open(f'./nhl_stats/{self.get_date(1)}.json') as f:
                self.recent_data = json.load(f)
        except FileNotFoundError:
            print(f"No data found for {self.get_date(1)}")
            pass

    def read_data(self, data_file):
        if data_file == 'starting_goalies':
            return self.starting_goalies

    def write_data(self, data, save_to):
        date = self.get_date(0)
        if save_to == 'perm':
            json_file = f'./nhl_stats/{date}.json'
        elif save_to == 'temp':
            json_file = f'./nhl_stats/temp.json'
        elif save_to == 'starting_goalies':
            json_file = f'./starting_goalies.json'
        elif save_to == 'matchups':
            json_file = f'./matchups/matchups_{self.get_date(0)}.json'
        elif save_to == 'injuries':
            json_file = f'./injuries.json'
        with open(json_file, 'w', encoding='utf8') as jf:
            json.dump(data, jf, ensure_ascii=False)

    def get_date(self, days):
        date = datetime.datetime.now()
        if (date.day - days) < 1:
            month = date.month - 1
            if month == 2:
                day = (date.day - days) + 28
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                day = (date.day - days) + 31
            else:
                day = (date.day - days) + 30
            return f'{month}-{day}-{date.year}'
        else:
            return f'{date.month}-{date.day-days}-{date.year}'

    def get_player_team(self, player):
        teams = self.recent_data['teams']
        for team in teams:
            if player in teams[team]:
                return team
        return 0

    def get_page_source(self, url, sleep_time):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(
            "/Users/user/Documents/chromedriver", options=options)
        driver.get(url)
        time.sleep(sleep_time)  # Let the user actually see something!
        html = driver.page_source
        driver.quit()

        return html

    def get_matchups(self, matches):
        matchups = []
        for match in matches:
            match = match.split(' at ')
            if "St Louis Blues" in match:
                n = 0
                for team in match:
                    if team == "St Louis Blues":
                        match[n] = "St. Louis Blues"
            if "Montreal Canadiens" in match:
                n = 0
                for team in match:
                    if team == "Montreal Canadiens":
                        match[n] = "Montréal Canadiens"
            matchups.append(match)
        return matchups
