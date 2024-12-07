from statistics import Statistics
from query_builder import QueryBuilder
from player_reader import PlayerReader


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # Use separate QueryBuilder instances for each query
    query_m1 = QueryBuilder()
    query_m2 = QueryBuilder()
    query = QueryBuilder()

    m1 = (
        query_m1.plays_in("PHI")
        .has_at_least(10, "assists")
        .has_fewer_than(10, "goals")
        .build()
    )

    m2 = query_m2.plays_in("EDM").has_at_least(50, "points").build()

    matcher = query.one_of(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
