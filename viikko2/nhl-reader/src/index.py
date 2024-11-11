from playerutils import PlayerReader, PlayerStats
from ui import UI

def main():
    sovellus = UI()
    sovellus.run()

    season = sovellus.season_input
    country = sovellus.country_input

    url_custom = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    reader = PlayerReader(url_custom)
    stats = PlayerStats(reader.get_players())
    players = stats.top_scorers_by_nationality(country)

    sovellus.print_table(players)

if __name__ == "__main__":
    main()
