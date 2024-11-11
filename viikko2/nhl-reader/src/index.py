import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)
    players_by_country = {}

    for player_dict in response:
        player = Player(player_dict)
        country = player_dict['nationality']

        if country not in players_by_country:
            players_by_country[country] = []

        players_by_country[country].append(player)

    print("Oliot:")

    for country in players_by_country.keys():
        print("Players from", country, "\n")
        country_list = players_by_country[country]
        for player in sorted(country_list, key=lambda player: player.total, reverse=True):
            print(player)
        print("")

if __name__ == "__main__":
    main()
