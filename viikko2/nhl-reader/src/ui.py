from rich.console import Console
from rich import print
from rich.table import Table

class UI:
    def __init__(self):
        self.seasons = ["2018-19", "2019-20", "2020-21", "2021-22", 
                        "2022-23", "2023-24", "2024-25"]
        self.countries = ["AUT", "CZE", "AUS", "SWE", "GER", "DEN", 
                          "SUI", "SVK", "NOR", "RUS", "CAN", "LAT", 
                          "BLR", "SLO", "USA", "FIN", "GBR"]
        self.season_input = None
        self.country_input = None

        self.console = Console()

    def start(self):
        self.console.print("[italic]NHL statistics by season and nationality[/italic]")

    def print_table(self, players):
        table_data = []

        for player in players:
            table_data.append(
                [
                    f"[cyan]{player[0]}",
                    f"[magenta]{player[1]}",
                    f"[green]{player[2]}",
                    f"[green]{player[3]}",
                    f"[green]{player[4]}",
                ],
            )

        table = Table(title=f"Top scorers of {self.country_input} season {self.season_input}", show_footer=False)

        table.add_column("Player name", no_wrap=True)
        table.add_column("Team", no_wrap=True)
        table.add_column("Goals", no_wrap=True)
        table.add_column("Assists", no_wrap=True)
        table.add_column("Points", no_wrap=True)

        for row in table_data:
            table.add_row(*row)

        table.width = self.console.measure(table).maximum

        table.width = None

        self.console.print(table)

        self.console.print("")

    def run(self):
        self.start()

        season = self.console.input("Select season \n [b purple][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25][/b purple]: ")
        if season not in self.seasons:
            self.console.print("Virheellinen syöte")
            return
        else:
            self.season_input = season

        self.console.print("")

        country = self.console.input("Select nationality \n [b purple][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/b purple]: ")
        if country not in self.countries:
            self.console.print("Virheellinen syöte")
            return
        else:
            self.country_input = country