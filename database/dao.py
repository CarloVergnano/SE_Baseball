from database.DB_connect import DBConnect
from model.teams import Team

class DAO:
    @staticmethod
    def query_esempio():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM esempio """

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    def get_teams(anno):
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                select t.id, t.`year`, t.name, t.team_code, sum(s.salary) as ingaggi
                from team t, salary s 
                where t.`year` = %s and s.team_id = t.id 
                group by t.id 
                """
        try:
            cursor.execute(query, (anno,))
            for row in cursor:
                team = Team(
                    id=row["id"],
                    year=row["`year`"],
                    name=row["name"],
                    team_code = row["team_code"],
                    ingaggi = row["ingaggi"]
                )
                result.append(team)

        except Exception as e:
            print(f"Errore durante la query get_album: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_years():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """
                       select distinct `year` 
                        from team
                        where `year` > 1979 
                        """
        try:
            cursor.execute(query,)
            for row in cursor:
                result.append(row["year"])

        except Exception as e:
            print(f"Errore durante la query get_playlist: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result