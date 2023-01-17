from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    def import_data(path, type):
        if path.endswith(".csv"):
            return Inventory.open_csv(path, type)
        elif path.endswith(".json"):
            return Inventory.read_json(path, type)

    def read_json(path, type):
        with open(path) as file:
            dict_list = json.loads(file.read())

        if type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)

    def open_csv(path, type):
        with open(path) as file:
            dict_list = list(csv.DictReader(file))
        if type == "simples":
            return SimpleReport.generate(dict_list)
        else:
            return CompleteReport.generate(dict_list)
