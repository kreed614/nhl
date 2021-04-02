from predict_ga import Predict_GA
from misc_functions import Misc_Functions


def test_predict_ga():
    pg = Predict_GA(["C.Chris Driedger", "J.Jake Oettinger"], [
                    ['Florida Panthers', 1.3899], ['Dallas Stars', 1.4974]])
    test_opposing_scores = pg._get_opposing_scores()
    if test_opposing_scores == [['J.Jake Oettinger', 1.3899], ['C.Chris Driedger', 1.4974]]:
        print("Opposing Scores: PASS")
    else:
        print("Opposing Scores: FAIL")
        print(f'Returned: {test_opposing_scores}')
        print(
            "Expected: [['J.Jake Oettinger', 1.3899], ['C.Chris Driedger', 1.4974]]")


def test_get_matchups():
    mf = Misc_Functions()
    matches = {"Philadelphia Flyers at Buffalo Sabres": ["B.Brian Elliott", "L.Linus Ullmark"], "New York Islanders at Pittsburgh Penguins": ["S.Semyon Varlamov", "T.Tristan Jarry"], "Edmonton Oilers at Toronto Maple Leafs": ["M.Mike Smith", "M.Michael Hutchinson"], "Anaheim Ducks at Colorado Avalanche": [
        "R.Ryan Miller", "P.Philipp Grubauer"], "Winnipeg Jets at Calgary Flames": ["C.Connor Hellebuyck", "J.Jacob Markstrom"], "Los Angeles Kings at Vegas Golden Knights": ["J.Jonathan Quick", "R.Robin Lehner"], "Minnesota Wild at San Jose Sharks": ["C.Cam Talbot", "M.Martin Jones"]}
    test_matchups = mf.get_matchups(matches)
    result = [["Philadelphia Flyers", "Buffalo Sabres"], ["New York Islanders", "Pittsburgh Penguins"], ["Edmonton Oilers", "Toronto Maple Leafs"], [
        "Anaheim Ducks", "Colorado Avalanche"], ["Winnipeg Jets", "Calgary Flames"], ["Los Angeles Kings", "Vegas Golden Knights"], ["Minnesota Wild", "San Jose Sharks"]]
    if test_matchups == result:
        print("Matchups: PASS")
    else:
        print("Matchups: FAIL")
        print(f'Returned: {test_matchups}')
        print("Expected: [['Philadelphia Flyers', 'Buffalo Sabres'], ['New York Islanders', 'Pittsburgh Penguins'], ['Edmonton Oilers', 'Toronto Maple Leafs'], [ \
            'Anaheim Ducks', 'Colorado Avalanche'], ['Winnipeg Jets', 'Calgary Flames'], ['Los Angeles Kings', 'Vegas Golden Knights'], ['Minnesota Wild', 'San Jose Sharks']]")


def main():
    test_predict_ga()
    test_get_matchups()


main()
