class Tournament:
    def __init__(self, name, start_date, end_date) -> None:
        self.name = name
        self.date = (start_date, end_date)

    def __str__(self) -> str:
        return f"{self.name}, date: {self.date}"
