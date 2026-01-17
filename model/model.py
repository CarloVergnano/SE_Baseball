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

    def get_teams(self, anno):
        self.teams = DAO.get_teams(anno)
        return self.teams

    def crea_grafo (self):
        self.G.clear()
        for team1 in self.teams:
            for team2 in self.teams:
                peso = team1.ingaggi + team2.ingaggi
                self.G.add_edge(team1.id, team2.id, weight=peso)

        return self.G








