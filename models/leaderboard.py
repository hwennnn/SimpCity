"""
This module deals with all leaderboard related functions.
"""
__docformat__ = "google"

from models.leaderboard_player import LeaderboardPlayer
from models.configurations import savedLeaderboardFilename
from models.utils import current_ms
from bisect import bisect_right
import os


class Leaderboard:
    leaderboard: list[LeaderboardPlayer]
    """A list of leaderboard player in descending order"""

    def __init__(self):
        """
        Initialise the leaderboard object with empty leaderboard array, 
        then call another method to load leaderboard from the file.
        """
        self.leaderboard = []
        self.loadLeaderboardFromFile()

    def loadLeaderboardFromFile(self):
        """
        The method will update the leaderboard array from the saved leaderboard file if there is any valid one.
        """

        if not self.isSavedLeaderboardExist():
            return

        lines = self.readFiles()

        isFileValid, loadedLeaderboard = self.isSavedLeaderboardFileValid(
            lines)
        if isFileValid:
            self.leaderboard = loadedLeaderboard

    def readFiles(self):
        """
        Returns:
            list[str]: An array of string

        The method will read the lines from the saved leaderboard file.
        """

        lines = None

        with open(savedLeaderboardFilename, "r+") as file:
            lines = file.readlines()

        return lines

    def saveScoreIntoLeaderboard(self, playerScore, defaultPlayerName=""):
        """
        Args:
            playerScore (int): The score of the player
            defaultPlayerName (str): An optional value for the name of the player


        The method will first calculate the ranking of the player, 
        then it will prompt the user to enter his/her username if the player scores top 10 in the leaderboard. \n
        After that, it will append the player to the leaderboard then save the latest result into the default leaderboard file.
        """

        # 1-indexed ranking
        ranking = 1 + self.getRankingInLeaderBoard(playerScore)

        if ranking > 10:
            print("Sorry! You didn't make it to top 10 in the leaderboard!")
        else:
            print(
                f"Congratulations! You made the high score board at position {ranking}!")

            playerName = defaultPlayerName

            # While loop condition: The player name must not be empty and should not exceed 20 characters.
            while len(playerName) == 0 or len(playerName) > 20:
                playerName = input("Please enter your name (max 20 chars): ")

            self.appendScoreIntoLeaderboard(playerName, playerScore)
            self.saveLatestLeaderboardIntoFile()

    def appendScoreIntoLeaderboard(self, playerName, playerScore):
        """
        Args:
            playerName (str): The name of the player
            playerScore (int): The score of the player

        The method will append the leaderboard player object to the current leaderboard array, and sort them in descending order (of score), \n
        If it satisfies any of the condition below:
        - There are less than 10 players in the current leaderboard
        - The current leaderboard has 10 players and the player score is higher than any of the player in the current leaderboard

        """

        if (0 <= len(self.leaderboard) <= 9):
            # There are less than 10 players in the current leaderboard
            currentMs = current_ms()
            self.leaderboard.append(LeaderboardPlayer(
                playerName, playerScore, currentMs))
            self.leaderboard.sort(
                key=lambda player: (-player.score, player.recordedTime, player.name))

        elif (playerScore > self.leaderboard[-1].score):
            # pop the player from the leaderboard as the new playerScore is higher than his
            self.leaderboard.pop()

            currentMs = current_ms()
            self.leaderboard.append(LeaderboardPlayer(
                playerName, playerScore, currentMs))
            self.leaderboard.sort(
                key=lambda player: (-player.score, player.recordedTime, player.name))

    def getRankingInLeaderBoard(self, playerScore):
        """
        Args:
            playerScore (int): The score of the player

        The method will retrieve the ranking of the player in the current leaderboard using binary search. \n
        For examples, the scores array is [-10, -9, -7]. \n
        By using bisect_right module and inverting the integer, 
        we can find the insertion point, hence knowing the player will be 3rd place in the leaderboard if his score is 8 (-8).
        """

        scores = [-player.score for player in self.leaderboard]

        ranking = bisect_right(scores, -playerScore)

        return ranking

    def parseLeaderboardAsStringArray(self):
        """
        Returns:
            list[str]: An array of string

        The method will loop through the leaderboard array and append a formatted line consisting of
        the name, score, recordedTime of the player.
        """

        lines = []

        for player in self.leaderboard:
            playerName, playerScore, recordedTime = player.name, player.score, player.recordedTime
            lines.append(f"{playerName}, {playerScore}, {recordedTime}")

        return lines

    def saveLatestLeaderboardIntoFile(self):
        """
        The method will write the parsed leadeboard string array into the leaderboard file.
        """

        with open(savedLeaderboardFilename, 'w+') as f:
            leaderboardLines = self.parseLeaderboardAsStringArray()

            for line in leaderboardLines:
                f.writelines(line + "\n")

    def displayLeaderboard(self):
        """
        The method will display the leaderboard.
        """

        leaderboardContent = [
            "\n--------- HIGH SCORES ---------",
            "Pos Player                Score",
            "--- ------                -----",
        ]
        maxLineWidth = len(leaderboardContent[0])

        for ranking, player in enumerate(self.leaderboard, 1):
            header = " " * int(ranking != 10) + f"{ranking}. {player.name}"
            trailing = f"{player.score}"
            spacesCount = maxLineWidth - len(header) - len(trailing)
            middleSpaces = " " * spacesCount

            leaderboardContent.append(header + middleSpaces + trailing)

        leaderboardContent.append("-------------------------------")

        print("\n".join(leaderboardContent))

    def isSavedLeaderboardExist(self):
        """
        Returns:
            bool: The result whether the leaderboard file does exist or not

        The method will check whether the leaderboard file does exist or not in the current directory.
        """

        return os.path.exists(savedLeaderboardFilename)

    def isLeaderboardPlayerNameValid(self, playerName):
        """
        Returns:
            bool: The result whether is the player name valid

        The method will check whether the name of the player is valid or not
        """

        return 1 <= len(playerName) <= 20

    def isSavedLeaderboardFileValid(self, lines):
        """
        Returns:
            tuple(bool, list[str]): (The result whether is the leaderboard file valid, the loaded leaderboard content)

        The method will check whether the leaderboard file is valid,
        and it will return the loaded leaderboard result if the file is valid.
        """

        # leaderboard file will have at most 10 lines
        if len(lines) > 10:
            return (False, None)

        results = []

        for line in lines:
            playerName, playerScore, recordedTime = line.strip("\n").split(',')

            if self.isLeaderboardPlayerNameValid(playerName):
                results.append(LeaderboardPlayer(
                    playerName, int(playerScore), int(recordedTime)))
            else:
                return (False, None)

        return (True, results)
