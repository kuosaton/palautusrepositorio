from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
    
    def get_players(self):
        players_by_country = {}
        encountered_player_ids = set()

        for player_dict in self.response:
            player = Player(player_dict)
            country = player_dict['nationality']

            if country not in players_by_country:
                players_by_country[country] = set()

            if player.id not in encountered_player_ids:
                encountered_player_ids.add(player.id)
                players_by_country[country].add(player)

        return players_by_country

class PlayerStats:
    def __init__(self, players_dict):
        self.players_dict = players_dict

    def top_scorers_by_nationality(self, country=None):
        # If a country is not given, this function returns all players grouped by nationality

        result = []

        if country is not None:
            country_players = self.players_dict[country]
            result.append(f"Players from {country} \n")

            for player in sorted(country_players, key=lambda player: player.total, reverse=True):
                result.append(player)
        
        else:
            for country in self.players_dict.keys():
                result.append(f"Players from {country} \n")
                country_players = self.players_dict[country]

                for player in sorted(country_players, key=lambda player: player.total, reverse=True):
                    result.append(player)

                result.append("")

        return result
