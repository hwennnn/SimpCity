"""
This module deals with all leaderboard player related functions.
"""
__docformat__ = "google"


class LeaderboardPlayer:
    name: str
    """The name of the leaderboard player"""
    score: str
    """The score of the leaderboard player"""
    recordedTime: int
    """The time recorded when it's being saved into the file"""

    def __init__(self, name, score, recordedTime):
        """
        Initialise the leaderboard player object with name, score and recorded time.
        """
        self.name = name
        self.score = score
        self.recordedTime = recordedTime
