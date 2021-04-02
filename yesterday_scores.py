from misc_functions import Misc_Functions
from bs4 import BeautifulSoup


class Yesterday_Scores():

    def _get_team_name(self, region):
        if region == 'Anaheim':
            return 'Anaheim Ducks'
        elif region == 'Arizona':
            return 'Arizona Coyotes'
        elif region == 'Vancouver':
            return 'Vancouver Canucks'
        elif region == 'Boston':
            return 'Boston Bruins'
        elif region == 'Nashville':
            return 'Nashville Predators'
        elif region == 'St. Louis':
            return 'St. Louis Blues'
        elif region == 'Calgary':
            return 'Calgary Flames'
        elif region == 'Buffalo':
            return 'Buffalo Sabres'
        elif region == 'Carolina':
            return 'Carolina Hurricanes'
        elif region == 'Chicago':
            return 'Chicago Blackhawks'
        elif region == 'Colorado':
            return 'Colorado Avalanche'
        elif region == 'Dallas':
            return 'Dallas Stars'
        elif region == 'Detroit':
            return 'Detroit Red Wings'
        elif region == 'Edmonton':
            return 'Edmonton Oilers'
        elif region == 'Florida':
            return 'Florida Panthers'
        elif region == "Los Angeles":
            return 'Los Angeles Kings'
        elif region == "Minnesota":
            return 'Minnesota Wild'
        elif region == "Montreal":
            return 'Montréal Canadiens'
        elif region == "New Jersey":
            return 'New Jersey Devils'
        elif region == "NY Islanders":
            return 'New York Islanders'
        elif region == "NY Rangers":
            return 'New York Rangers'
        elif region == 'Ottawa':
            return "Ottawa Senators"
        elif region == 'Philadelphia':
            return "Philadelphia Flyers"
        elif region == 'Pittsburgh':
            return "Pittsburgh Penguins"
        elif region == 'San Jose':
            return "San Jose Sharks"
        elif region == 'Columbus':
            return "Columbus Blue Jackets"
        elif region == 'Tampa Bay':
            return "Tampa Bay Lightning"
        elif region == 'Vegas':
            return "Vegas Golden Knights"
        elif region == 'Washington':
            return "Washington Capitals"
        elif region == "Winnipeg":
            return 'Winnipeg Jets'
        else:
            return region

    def get_scores(self):
        mf = Misc_Functions()
        html = open('results_test.html', "r")
        # html = mf.get_page_source(
        #     f'http://www.nhl.com/ice/m_scores.htm', 1)
        soup = BeautifulSoup(html, 'html.parser')
        scores = []
        matches = soup.find_all('table', class_='gmDisplay finalState')
        for match in matches:
            contents = match.find_all('tr')
            n = 0
            for content in contents:
                if n == 0:
                    pass
                else:
                    content = content.get_text().split('\n').remove('')
                    content[1] = content[1][0]
                    scores.append(content)
                n += 1
        n = 0
        temp_result, result = [], []
        for score in scores:
            temp_result.append(score)
            if n == 1:
                result.append(temp_result)
                temp_result = []
                n = -1
            n += 1
        print(result)
        for n in result:
            print(n)


ys = Yesterday_Scores()
ys.get_scores()
