from goalie_functions import Goalie_Functions
from misc_functions import Misc_Functions
import numpy as np
from sklearn.linear_model import LinearRegression
import os


class Predict_GA():
    def __init__(self, goalies, offenses):
        self.goalie = Goalie_Functions()
        self.misc = Misc_Functions()
        self.goalies = goalies
        self.offenses = offenses

    def _get_opposing_score(self, goalie):
        team = self.misc.get_player_team(goalie)
        for offense in self.offenses:
            if team != offense[0]:
                return float(offense[1])

    def get_prediction(self, array_x, array_y, offense_score):
        x = np.array(array_x).reshape((-1, 1))
        y = np.array(array_y)
        model = LinearRegression()
        model.fit(x, y)
        if model.coef_ < 0:
            return -1
        return float(model.coef_ * offense_score + model.intercept_)

    def get_ga(self):
        predictions = []
        for goalie in self.goalies:
            performances = self.goalie.get_goalie_past_performance(
                [goalie], (len(os.listdir('./matchups'))-1))
            array_x, array_y = [], []
            for performance in performances:
                if performance[3] != 'N/A':
                    array_x.append(performance[4])
                    array_y.append(performance[3])
            if len(array_x) > 1:
                opposing_score = self._get_opposing_score(goalie)
                prediction = self.get_prediction(
                    array_x, array_y, opposing_score)
            else:
                continue

            if prediction > 0:
                predictions.append([goalie, prediction])
        return predictions
