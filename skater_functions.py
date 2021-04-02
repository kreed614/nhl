from misc_functions import Misc_Functions


class Skater_Functions():
    def __init__(self):
        self.mf = Misc_Functions()

    def get_skater_score(self, skater: dict[str, int]) -> int:
        # returns a score to rate skaters against one another
        g = int(skater['g'])
        ppg = int(skater['ppg'])
        s = int(skater['s'])
        shg = int(skater['smg'])  # smg was a typo
        gp = int(skater['gp'])
        pm = int(skater['+/-'])
        if gp > 0 and s > 0:
            score = (1 + (g - (ppg * .5) + (shg * 1.3))/s) + (pm * (g/gp))
        elif s == 0:
            score = 0
        return score

    def get_offense_score(self, input_list: list[str]) -> list[str]:
        result = []
        for element in input_list:
            if element == 'Montreal Canadiens':
                element = 'Montréal Canadiens'
            if element == 'St Louis Blues':
                element = 'St. Louis Blues'
            averages, scores = {}, []
            averages[element] = {}
            for player in self.mf.recent_data['teams'][element]:
                # hacky way to isolate skaters from goalies
                if len(self.mf.recent_data['teams'][element][player]) > 14:
                    score = self.get_skater_score(
                        self.mf.recent_data['teams'][element][player])
                    if player in self.mf.injuries_data:
                        if score > 10:
                            print(
                                f'[INJURED] {player} ({"{:.2f}".format(score)})')
                        continue
                    else:
                        scores.append(score)
            averages[element] = sum(scores) / len(scores)
            for element in averages:
                result.append([element, "{:.4f}".format(averages[element])])

        return result

        # pct = (1-(other_offense/best_offense))*100
        # print(
        #     f'{result} offense is better by {"{:.2f}".format(pct)}%')
