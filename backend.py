import sqlite3

PREMIER_LEAGUE = ["Liverpool", "Manchester City", "Arsenal", "Manchester Utd", "Wolves", "Leicester", "Chelsea",
                  "Sheffield Utd", "Tottenham", "Burnley", "Crystal Palace", "Everton", "Newcastle", "Southampton",
                  "Brighton", "West Ham", "Watford", "Bournemouth", "Aston Villa", "Norwich"]

LIGUE_ONE = ["PSG", "Marsylia", "Rennes", "Lille", "Reims", "Nice", "Lyon", "Montpellier", "Monaco", "Angers", "Strasbourg",
             "Bordeaux", "Nantes", "Brest", "Metz", "Dijon", "St. Etienne", "Nimes", "Amiens", "Toulouse"]

LA_LIGA = ["Barcelona", "Real Madryt", "Sevilla", "Real Sociedad", "Getafe", "Atl. Madryt", "Valencia", "Villarreal", "Granada",
           "Ath. Bilbao", "Osasuna", "Betis", "Levante", "Alaves", "Valladolid", "Eibar", "Celta Vigo", "Mallorca", "Leganes",
           "Espanyol"]

BUNDESLIGA = ["Bayern", "Dortmund", "RB Lipsk", "Moenchengladbach", "Leverkusen", "Schalke", "Wolfsburg", "Freiburg", "Hoffenheim",
              "FC Koeln", "Union Berlin", "Frankfurt", "Hertha", "Augsburg", "Mainz", "Düsseldorf", "Bremen", "Paderborn"]

SERIE_A = ["Juventus", "Lazio", "Inter", "Atalanta", "AS Roma", "Napoli", "AC Milan", "Verona", "Parma", "Bologna", "Sassuolo",
           "Cagliari", "Fiorentina", "Udinese", "Torino", "Sampdoria", "Genoa", "Lecce", "Spal", "Brescia"]


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("teams.db")
        self.cur = self.conn.cursor()
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM teams")
        rows=self.cur.fetchall()
        return rows

    def find_by_name(self, name=""):
        self.cur.execute("SELECT * FROM teams WHERE name=?", (name,))
        rows = self.cur.fetchall()
        return rows


    def __del__(self):
        self.conn.close()