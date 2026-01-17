import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.anni = []
        self.teams = []

    def get_anni(self):
        self.anni = DAO.get_years()
        return self.anni

    def get_team(self, anno):
        self.teams = DAO.get_teams(anno)
        return self.teams

    def crea_grafo (self, anno):
        self.G.clear()
        self.teams = DAO.get_teams(anno)
        self.sorted_teams = sorted(self.teams, key=lambda team: team.ingaggi, reverse=True)
        for team1 in self.sorted_teams:
            for team2 in self.sorted_teams:
                if team1 != team2:
                    peso = team1.ingaggi + team2.ingaggi
                    self.G.add_edge(team1.id, team2.id, weight=peso)



        return self.G

    def getVicini(self, squadra_id):
        neighbors = list(self.G.neighbors(squadra_id))
        return neighbors








