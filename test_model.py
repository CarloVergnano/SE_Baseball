from model.model import Model
m = Model()
m.get_team(2015)
grafo = (m.crea_grafo(2015))
print(grafo.edges)



vicini = m.getVicini(2777)

print (vicini)