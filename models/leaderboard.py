from models.leaderboard_player import LeaderboardPlayer
from models.configurations import savedLeaderboardFilename
import os


class Leaderboard:
    def __init__(self):
        self.leaderboard = []

    def loadLeaderboardFromFile(self):
        pass

    def saveScoreIntoLeaderboard(self):
        pass

    def displayLeaderboard(self):
        pass

    def isSavedLeaderboardExist(self):
        pass

    def isSavedLeaderboardFileValid(self, lines):
        pass
