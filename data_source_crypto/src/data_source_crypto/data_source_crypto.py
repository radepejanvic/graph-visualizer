import json
from api.src.api.services.base import DataSourceBase
from api.src.api.models.model import *

class CryptoDataSource(DataSourceBase):
    def identifier(self) -> str:
        return "CryptoDataSource"

    def name(self) -> str:
        return "CryptoDataSource"

    def load(self) -> Graph:

        data = []
        with open('../data_source_crypto/src/data_source_crypto/crypto.json', 'r') as file:
            data = json.load(file)

        graph = Graph()
        for item in data:
            from_owner = item["from_owner"]
            to_owner = item["to_owner"]
            owner_to = item["from_address"][:10]
            address_to = item["to_address"][:10]
            graph.add_branch(Node(owner_to, {"name": owner_to, "from_owner": from_owner}),
                            Node(address_to, {"name": address_to, "to_owner": to_owner}),
                            {"name": address_to}, True)

        return graph
