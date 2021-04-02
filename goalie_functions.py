from misc_functions import Misc_Functions
from skater_functions import Skater_Functions
import json


class Goalie_Functions():
    def __init__(self):
        self.mf = Misc_Functions()

    def get_goalie_score(self, matchup: list[str]) -> list[str]:
        result = []
        for goalie in matchup:
            score = 0
            try:
                svp = float(self.mf.recent_data['goalies'][goalie]['sv%'])
                so = float(self.mf.recent_data['goalies'][goalie]['so'])
                l = int(self.mf.recent_data['goalies'][goalie]['l'])
                gs = int(self.mf.recent_data['goalies'][goalie]['gs'])
                ga = int(self.mf.recent_data['goalies'][goalie]['ga'])
                sa = int(self.mf.recent_data['goalies'][goalie]['sa'])
                if ga == 0:
                    score = ((gs)+(svp) + sa)*(1 + so*.25)
                elif l == 0:
                    score = ((gs)+(svp)+(sa/ga))*(1 + so*.25)
                else:
                    score = ((gs/l)+(svp)+(sa/ga))*(1 + so*.25)

            except KeyError:
                print(f'No data for {goalie}')
                continue

            team = self.mf.get_player_team(goalie)
            result.append([goalie, team, "{:.2f}".format(score)])
        return result

    def _get_goalie_last_matchup(self, data, i, team, n):
        offense = Skater_Functions()
        matchup = f'./matchups/matchups_{self.mf.get_date(n - i)}.json'
        opposing_team = str
        with open(matchup) as f:
            matchup_data = json.load(f)
        for element in matchup_data:
            if team in element:
                for teams in element:
                    if element == team:
                        pass
                    opposing_team = team
                continue

        result = []
        try:
            for skater in data['teams'][opposing_team]:
                try:
                    result.append(offense.get_skater_score(
                        data['teams'][opposing_team][skater]))
                except:
                    continue
            return sum(result)/len(result)
        except KeyError:
            return 0

    def get_goalie_past_performance(self, matchup: list[str], n: int = 7) -> list[str]:
        result = []
        for goalie in matchup:
            last_gp, last_ga, gaa = 0, 0, 0
            team = self.mf.get_player_team(goalie)
            for i in range(n):
                current_file = f'./nhl_stats/{self.mf.get_date(n - i)}.json'
                with open(current_file) as f:
                    data = json.load(f)
                try:
                    gp = data['goalies'][goalie]['gp']
                    ga = data['goalies'][goalie]['ga']
                    gaa = data['goalies'][goalie]['gaa']
                except KeyError:
                    continue
                if last_gp == 0:
                    last_gp, last_ga = gp, ga
                    continue
                if gp == last_gp:
                    result.append(
                        [goalie, gaa, self.mf.get_date(n - i), 'N/A', 'N/A'])
                else:
                    self._get_goalie_last_matchup(data, i, team, n)
                    result.append([goalie, gaa, self.mf.get_date(
                        n - i), int(ga) - int(last_ga), self._get_goalie_last_matchup(data, i, team, n)])
                    last_ga, last_gp = ga, gp
        return result
