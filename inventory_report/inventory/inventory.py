from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path, encoding="utf-8") as file:
            inventory_products = csv.DictReader(file)
            if report_type == "simples":
                return SimpleReport.generate(list(inventory_products))
            elif report_type == "completo":
                return CompleteReport.generate(list(inventory_products))
            else:
                print('o valor dever ser "simples" ou "completo"')
                raise ValueError("Type invalid")
