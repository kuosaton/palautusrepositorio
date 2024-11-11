class Player:
    def __init__(self, dict):
        self.nationality = dict['nationality']
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.total = (self.goals + self.assists)
        self.games = dict['games']
        self.id = dict['id']

    def __str__(self):
        return f"{self.name:25} {self.team:15} {self.goals:3}  + {self.assists:3}  = {self.total:3}, games: {self.games:2}"
