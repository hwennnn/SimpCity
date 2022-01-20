from models.leaderboard_player import LeaderboardPlayer
from models.configurations import savedLeaderboardFilename
from models.utils import current_ms
from bisect import bisect_right
import os


class Leaderboard:
    def __init__(self):
        self.leaderboard = []
        self.loadLeaderboardFromFile()

    def loadLeaderboardFromFile(self):
        if not self.isSavedLeaderboardExist():
            return

        lines = self.readFiles()

        isFileValid, loadedLeaderboard = self.isSavedLeaderboardFileValid(
            lines)
        if isFileValid:
            self.leaderboard = loadedLeaderboard
            print('Successfully loaded the leaderboard!')

    def readFiles(self):
        lines = None

        with open(savedLeaderboardFilename, "r+") as file:
            lines = file.readlines()

        return lines

    def saveScoreIntoLeaderboard(self, playerScore, defaultPlayerName=""):
        # 1-indexed
        ranking = self.getRankingInLeaderBoard(playerScore)

        if ranking > 10:
            print("Sorry! You didn't make it to top 10 in the leaderboard!")
        else:
            print(
                f"Congratulations! You made the high score board at position {ranking}!")

            playerName = defaultPlayerName

            while len(playerName) == 0 and len(playerName) > 20:
                playerName = input("Please enter your name (max 20 chars): ")

            self.appendScoreIntoLeaderboard(playerName, playerScore)
            self.saveLatestLeaderboardIntoFile()

    def appendScoreIntoLeaderboard(self, playerName, playerScore):
        if (0 <= len(self.leaderboard) <= 9):
            currentMs = current_ms()
            self.leaderboard.append(LeaderboardPlayer(
                playerName, playerScore, currentMs))
            self.leaderboard.sort(
                key=lambda player: (-player.score, player.recordedTime, player.name), reverse=1)

        elif (playerScore > self.leaderboard[-1].score):
            # pop the player from the leaderboard as the new playerScore is higher than his
            self.leaderboard.pop()

            currentMs = current_ms()
            self.leaderboard.append(LeaderboardPlayer(
                playerName, playerScore, currentMs))
            self.leaderboard.sort(
                key=lambda player: (-player.score, player.recordedTime, player.name), reverse=1)

    def getRankingInLeaderBoard(self, playerScore):
        scores = [player.score for player in self.leaderboard]

        ranking = bisect_right(scores, playerScore)
        return 10 - ranking

    def parseLeaderboardAsStringArray(self):
        lines = []

        for player in self.leaderboard:
            playerName, playerScore, recordedTime = player.name, player.score, player.recordedTime
            lines.append(f"{playerName}, {playerScore}, {recordedTime}")

        return lines

    def saveLatestLeaderboardIntoFile(self):
        with open(savedLeaderboardFilename, 'w+') as f:
            leaderboardLines = self.parseLeaderboardAsStringArray()

            for line in leaderboardLines:
                f.writelines(line + "\n")

    def displayLeaderboard(self):
        leaderboardContent = [
            "--------- HIGH SCORES ---------",
            "Pos Player                Score",
            "--- ------                -----",
        ]
        maxLineWidth = len(leaderboardContent[0])

        for ranking, player in enumerate(self.leaderboard, 1):
            header = f" {ranking}. {player.name}"
            trailing = f"{player.score}"
            spacesCount = maxLineWidth - len(header) - len(trailing)
            middleSpaces = " " * spacesCount

            leaderboardContent.append(header + middleSpaces + trailing)

        leaderboardContent.append("--- ------                -----")

        print("\n".join(leaderboardContent))

    def isSavedLeaderboardExist(self):
        return os.path.exists(savedLeaderboardFilename)

    def isLeaderboardPlayerNameValid(self, playerName):
        return 1 <= len(playerName) <= 20

    def isSavedLeaderboardFileValid(self, lines):
        # leaderboard file will have at most 10 lines
        if len(lines) > 10:
            return (False, None)

        results = []

        for line in lines:
            playerName, playerScore, recordedTime = line.strip("\n").split(',')

            if self.isLeaderboardPlayerNameValid(playerName):
                results.append(LeaderboardPlayer(
                    playerName, int(playerScore), int(recordedTime)))

        return (True, results)
