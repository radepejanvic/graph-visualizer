from api.src.api.models.model import Graph, Node
from api.src.api.services.base import DataSourceBase
import xmltodict

import os


class FlightsDataSource(DataSourceBase):

    def identifier(self) -> str:
        return "FlightsDataSource"

    def name(self) -> str:
        return "FlightsDataSource"

    def load(self) -> Graph:
        with open("../data_source_xml/flightsWithInfo.xml", 'r+') as file:
            flights = xmltodict.parse(file.read(), encoding='utf-8')

        graph = Graph()

        for flight in flights['root']['flight']:
            dictionary = {}

            dictionary['carrier'] = flight['carrier']
            dictionary['flightNumber'] = flight['flightNumber']
            dictionary['aircraftType'] = flight['aircraftType']
            dictionary['departureDate'] = flight['departure']['date']
            dictionary['arrivalDate'] = flight['arrival']['date']

            departureDictionary = {}
            departureAirport = flight['departure']['airport']['iata']
            departureDictionary["City"] = flight['departure']['airport']['info']['city']
            departureDictionary["State"] = flight['departure']['airport']['info']['state']
            departureDictionary["Country"] = flight['departure']['airport']['info']['country']

            arrivalDictionary = {}
            arrivalAirport = flight['arrival']['airport']['iata']
            arrivalDictionary["City"] = flight['arrival']['airport']['info']['city']
            arrivalDictionary["State"] = flight['arrival']['airport']['info']['state']
            arrivalDictionary["Country"] = flight['arrival']['airport']['info']['country']

            graph.add_branch(Node(departureAirport, departureDictionary), Node(arrivalAirport, arrivalDictionary), dictionary, True)
        print(graph)
        return graph