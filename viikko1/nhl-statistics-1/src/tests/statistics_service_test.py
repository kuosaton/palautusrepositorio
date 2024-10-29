import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_works(self):
        self.assertEqual(str(self.stats.search("Kurri")), f"Kurri EDM 37 + 53 = 90")

    def test_search_returns_none(self):
        self.assertEqual(self.stats.search(f"A"), None)

    def test_team_returns_correct(self):
        self.assertEqual(str(self.stats.team("PIT")[0]), f"Lemieux PIT 45 + 54 = 99")

    def test_top_sorts_correctly(self):
        self.assertEqual(str(self.stats.top(4)[0]), f"Gretzky EDM 35 + 89 = 124")