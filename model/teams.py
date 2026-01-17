from dataclasses import dataclass

@dataclass()
class Team:
    id: int
    year: int
    name: str
    team_code: str
    ingaggi: int


    def __str__(self):
        return f"Team({self.id}, {self.year}, {self.name}, {self.team_code}, {self.ingaggi})"


    def __hash__(self):
        return hash(self.id)