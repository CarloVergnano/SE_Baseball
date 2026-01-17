from dataclasses import dataclass

@dataclass()
class Team:
    id: int
    year: int
    name: str
    team_code: str
    ingaggi: int


    def __str__(self):
        return f"Team(id={self.id})"

    def __repr__(self):
        return f"Team(id={self.id})"

    def __hash__(self):
        return hash(self.id)