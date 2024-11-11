from playerutils import PlayerReader, PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader.get_players())

    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
    
    
    all_players = stats.top_scorers_by_nationality()

    for player in all_players:
        print(player)

if __name__ == "__main__":
    main()
