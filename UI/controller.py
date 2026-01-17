import flet as ft
from networkx.algorithms.connectivity.edge_augmentation import weighted_bridge_augmentation

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.anno_selezionato = None
        self.squadra_selezionata = None
        self.vicini = []

    def on_anno_change(self, e):
        if e.control.value is None:
            return
        self.anno_selezionato = int(e.control.value)
        self.popola_dropdown_squadre()

    def popola_dropdown_anni(self):
        """Popola il menu a tendina delle regioni."""
        self._view.dd_anno.options.clear()

        anni = self._model.get_anni()

        if anni:
            for anno in anni:
                self._view.dd_anno.options.append(ft.dropdown.Option(key = anno, text=anno))
        else:
            self._view.show_alert("Errore nel caricamento anni.")

        self._view.update()


    def handle_crea_grafo(self, e):
        self.anno_selezionato = int(self._view.dd_anno.value)
        self.grafo = self._model.crea_grafo(int(self.anno_selezionato))
        self.teams = self._model.get_team(self.anno_selezionato)
        num_nodi = self.grafo.number_of_nodes()
        num_rami = self.grafo.number_of_edges()

        self._view.txt_out_squadre.controls.clear()
        self._view.txt_out_squadre.controls.append(
            ft.Text(f"Numero squadre: {num_nodi}")
        )

        for team in self.teams:
            self._view.txt_out_squadre.controls.append(
                ft.Text(f"({team.team_code}) {team.name}")
            )

        self._view.update()


    def on_squadra_change(self, e):
        self.squadra_selezionata = e.control.value

    def popola_dropdown_squadre(self):

        self._view.dd_squadra.options.clear()



        if self._view.dd_anno.value is None:
            self._view.show_alert("Seleziona prima un anno")
            return

        self.anno_selezionato = int(self._view.dd_anno.value)


        squadre = self._model.get_team(self.anno_selezionato)

        if not squadre:
            self._view.show_alert("Nessuna squadra trovata per l'anno selezionato")
            return
        if squadre:
            for squadra in squadre:
                self._view.dd_squadra.options.append(
                    ft.dropdown.Option(
                        key=squadra.id,
                        text=f"({squadra.team_code}) {squadra.name}"
                )
            )
        else:
            self._view.show_alert("Errore nel caricamento squadre.")


        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """
        print("Ciao")
        self._view.txt_risultato.controls.clear()
        team_id = int(self._view.dd_squadra.value)
        self.anno_selezionato = int(self._view.dd_anno.value)
        grafo = self._model.crea_grafo(self.anno_selezionato)
        vicini = self._model.getVicini(team_id)
        self.teams = self._model.get_team(self.anno_selezionato)
        self.sorted_teams = sorted(self.teams, key=lambda team: team.ingaggi, reverse=True)
        for team in self.sorted_teams:

            if team.id != team_id:
                peso = grafo[int(team_id)][int(team.id)]["weight"]
                self._view.txt_risultato.controls.append(
                    ft.Text(f"{team.team_code} ({team.name}) - peso {peso}")
                )

        self._view.update()




    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO