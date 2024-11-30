class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        """Awards a point for given player."""
        if player_name == "player1":
            self.player1.won_point()
        else:
            self.player2.won_point()

    def check_score_is_even(self):
        """Checks if player scores are even."""
        return self.player1.score == self.player2.score

    def check_score_exceeds_forty(self):
        """Checks if at least one player has a score of forty or more."""
        if self.player1.score >= 4 or self.player2.score >= 4:
            return True
        else:
            return False

    def calculate_score_difference(self):
        """Score difference calculated from the perspective of player 1."""
        return self.player1.score - self.player2.score

    def get_score_calls_under_forty(self):
        """When both players have a score under forty, this function is used to get score calls."""
        score = ""

        if self.check_score_is_even() == False:
            score_call_mapping = {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
                4: "Game",
            }

            player1_score_call = score_call_mapping[self.player1.score]
            player2_score_call = score_call_mapping[self.player2.score]

            score = f"{player1_score_call}-{player2_score_call}"

        else:
            if self.player1.score == 0:
                score = "Love-All"
            elif self.player1.score == 1:
                score = "Fifteen-All"
            elif self.player1.score == 2:
                score = "Thirty-All"
            else:
                score = "Deuce"

        return score

    def get_score_calls_forty_or_more(self):
        """When both players have a score of forty or more, this function is used to get score calls."""
        score = ""

        score_difference = self.calculate_score_difference()

        if score_difference == 1:
            score = "Advantage player1"
        elif score_difference == -1:
            score = "Advantage player2"
        elif score_difference >= 2:
            score = "Win for player1"
        elif score_difference <= -2:
            score = "Win for player2"
        else:
            score = "Deuce"

        return score

    def get_score(self):
        score = ""

        if self.check_score_exceeds_forty():
            score = self.get_score_calls_forty_or_more()
        else:
            score = self.get_score_calls_under_forty()

        return score
