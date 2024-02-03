import http.client
import json
from api.src.api.services.base import DataSourceBase
from api.src.api.models.model import *


# conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

# headers = {
#     'X-RapidAPI-Key': "a41f9b806fmsha2a7fbf5416f39dp18f015jsnb5ef97da598b",
#     'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
# }

# conn.request("GET", "/games?page=0&per_page=500", headers=headers)

# res = conn.getresponse()
# data = res.read().decode("utf-8")

class NBADataSource(DataSourceBase):
    def identifier(self) -> str:
        return "NBADataSource"

    def name(self) -> str:
        return "NBADataSource"

    def load(self) -> Graph:
        data = ('{"data":[{"id":47179,"date":"2019-01-30T00:00:00.000Z","home_team":{"id":2,"abbreviation":"BOS",'
                '"city":"Boston","conference":"East","division":"Atlantic","full_name":"Boston Celtics",'
                '"name":"Celtics"},"home_team_score":126,"period":4,"postseason":false,"season":2018,'
                '"status":"Final","time":" ","visitor_team":{"id":4,"abbreviation":"CHA","city":"Charlotte",'
                '"conference":"East","division":"Southeast","full_name":"Charlotte Hornets","name":"Hornets"},'
                '"visitor_team_score":94},{"id":48751,"date":"2019-02-09T00:00:00.000Z","home_team":{"id":2,'
                '"abbreviation":"BOS","city":"Boston","conference":"East","division":"Atlantic","full_name":"Boston '
                'Celtics","name":"Celtics"},"home_team_score":112,"period":4,"postseason":false,"season":2018,'
                '"status":"Final","time":"     ","visitor_team":{"id":13,"abbreviation":"LAC","city":"LA",'
                '"conference":"West","division":"Pacific","full_name":"LA Clippers","name":"Clippers"},'
                '"visitor_team_score":123},{"id":48739,"date":"2019-02-08T00:00:00.000Z","home_team":{"id":23,'
                '"abbreviation":"PHI","city":"Philadelphia","conference":"East","division":"Atlantic",'
                '"full_name":"Philadelphia 76ers","name":"76ers"},"home_team_score":117,"period":4,'
                '"postseason":false,"season":2018,"status":"Final","time":"     ","visitor_team":{"id":8,'
                '"abbreviation":"DEN","city":"Denver","conference":"West","division":"Northwest","full_name":"Denver '
                'Nuggets","name":"Nuggets"},"visitor_team_score":110},{"id":48740,"date":"2019-02-08T00:00:00.000Z",'
                '"home_team":{"id":30,"abbreviation":"WAS","city":"Washington","conference":"East",'
                '"division":"Southeast","full_name":"Washington Wizards","name":"Wizards"},"home_team_score":119,'
                '"period":4,"postseason":false,"season":2018,"status":"Final","time":"     ","visitor_team":{"id":6,'
                '"abbreviation":"CLE","city":"Cleveland","conference":"East","division":"Central",'
                '"full_name":"Cleveland Cavaliers","name":"Cavaliers"},"visitor_team_score":106},{"id":48746,'
                '"date":"2019-02-08T00:00:00.000Z","home_team":{"id":26,"abbreviation":"SAC","city":"Sacramento",'
                '"conference":"West","division":"Pacific","full_name":"Sacramento Kings","name":"Kings"},'
                '"home_team_score":102,"period":4,"postseason":false,"season":2018,"status":"Final","time":"     ",'
                '"visitor_team":{"id":16,"abbreviation":"MIA","city":"Miami","conference":"East",'
                '"division":"Southeast","full_name":"Miami Heat","name":"Heat"},"visitor_team_score":96}],'
                '"meta":{"current_page":1,"next_page":2,"per_page":5}}')
        data_json = json.loads(data)

        games = data_json.get("data", [])

        graph = Graph()

        for game in games:
            dictionary = {}
            game_id = game.get("id")
            date = game.get("date")

            home_team = game.get("home_team", {})
            home_team_full_name = home_team.get("full_name").replace(" ","_")
            home_team_score = game.get("home_team_score")

            visitor_team = game.get("visitor_team", {})
            visitor_team_full_name = visitor_team.get("full_name").replace(" ","_")
            visitor_team_score = game.get("visitor_team_score")

            dictionary["score"] = str(home_team_score) + ":" + str(visitor_team_score)
            dictionary["date"] = date
            graph.add_edge(Node(home_team_full_name, home_team), Node(visitor_team_full_name, visitor_team), dictionary)
        graph.printGraph()
        return graph
