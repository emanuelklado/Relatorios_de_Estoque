import csv
import json
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from xml.etree import ElementTree as ET


class Inventory:
    def read_xml(path, type):
        tree = ET.parse(path)
        root = list(tree.getroot())
        dictionary_list = []
        informations_dict = {}

        for index in range(len(root)):
            for info in root[index]:
                informations_dict[info.tag] = info.text

            dictionary_list.append(informations_dict)
            informations_dict = {}
        if type == "simples":
            return SimpleReport.generate(dictionary_list)
        else:
            return CompleteReport.generate(dictionary_list)

    def read_csv(path, type):
        with open(path) as file:
            dict_list = list(csv.DictReader(file))
        if type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

    def read_json(path, type):
        with open(path) as file:
            dict_list = json.loads(file.read())

        if type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

    def import_data(path, type):
        if path.endswith(".csv"):
            return Inventory.read_csv(path, type)
        elif path.endswith(".json"):
            return Inventory.read_json(path, type)
        elif path.endswith(".xml"):
            return Inventory.read_xml(path, type)
