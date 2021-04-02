from conceded_penalties import Conceded_Penalties
from predict_ga import Predict_GA
from injury_report import Injury_Report
from player_stats import Player_Stats
from skater_functions import Skater_Functions
from goalie_functions import Goalie_Functions
from starting_goalies import Starting_Goalies
from os import path
import sys
import time
import datetime
import os.path
import json
import asyncio
from misc_functions import Misc_Functions


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


async def main():
    mf = Misc_Functions()
    matchups = f'./matchups/matchups_{mf.get_date(0)}.json'
    today_data = f'./nhl_stats/{mf.get_date(0)}.json'
    yesterday_data = f'./nhl_stats/{mf.get_date(1)}.json'
    starting_goalies = mf.read_data('starting_goalies')

    def get_report():
        skaters = Skater_Functions()
        goalies = Goalie_Functions()
        matchup = []
        print(
            f'\n{bcolors.HEADER}{bcolors.BOLD}{datetime.datetime.now()}{bcolors.ENDC}\n \n')
        for matchups in starting_goalies:
            matchup = matchups.split(' at ')
            matchup[0], matchup[1] = matchup[0].strip(), matchup[1].strip()
            print(f'{bcolors.BOLD}{matchups}{bcolors.ENDC}')
            print('\nGoalie Performance')
            for gme_ds in goalies.get_goalie_past_performance(starting_goalies[matchups]):
                if gme_ds[3] == 'N/A':
                    print(
                        f'{gme_ds[0]} ({gme_ds[1]}) {gme_ds[2]}: {bcolors.WARNING}No Game{bcolors.ENDC}')
                else:
                    print(
                        f'{gme_ds[0]} ({gme_ds[1]}) {gme_ds[2]}: {gme_ds[3]} ga to a {"{:.4f}".format(gme_ds[4])} offense')
            print()
            for goalie in goalies.get_goalie_score(starting_goalies[matchups]):
                print(f'{goalie[0]} ({goalie[1]}): {goalie[2]}')
            print('\nOffensive Matchup')
            for offense in skaters.get_offense_score(matchup):
                print(offense[0], offense[1])
            print('\nEstimated Goals Against')
            pg = Predict_GA(
                starting_goalies[matchups], skaters.get_offense_score(matchup))
            print(pg.get_ga())
            print()

    if path.exists(yesterday_data) == False and datetime.datetime.now().hour < 16:
        players = Player_Stats()
        print(
            f'{bcolors.FAIL}Forgot to run yesterday\'s data. Be sure to change the file date and run again{bcolors.ENDC}')
        print('\n \n \n')
        players.write_daily_data()
        sys.exit(0)

    # Adjust hour based on when you want the goalie matchups
    # 15 should be standard time for weekdays
    if datetime.datetime.now().hour <= 8:
        mf = Misc_Functions()
        starters = Starting_Goalies()
        ir = Injury_Report()
        print('Refreshing Starting Goalies... \n')
        starting_goalies = starters.get_starting_goalies()
        print('Refreshing Injuries... \n')
        injuries = ir.get_injuries()
        mf.write_data(starting_goalies, "starting_goalies")
        mf.write_data(injuries, "injuries")
        if path.exists(matchups) == False:
            matchups = mf.get_matchups(starting_goalies)
            mf.write_data(matchups, "matchups")

    if path.exists(today_data) == False and datetime.datetime.now().hour > 20:
        players = Player_Stats()
        print()
        print(f'{bcolors.OKGREEN}Adding tonight\'s data{bcolors.ENDC}')
        print()
        time.sleep(2)
        players.write_daily_data()
        # also write scores data

    get_report()
    # cp = Conceded_Penalties()
    # cp.get_penalties('Anaheim Ducks')


if __name__ == "__main__":
    asyncio.run(main())
