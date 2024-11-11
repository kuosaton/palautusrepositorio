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
        return f"{self.name:20} {self.team:4} {self.goals:2} + {self.assists:2} = {self.total}"
