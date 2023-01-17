import csv
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, report_type: str) -> str:
        product_list = []
        with open(path) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                product_list.append(row)
        if report_type == "simples":
            return SimpleReport.generate(product_list)
        if report_type == "completo":
            return CompleteReport.generate(product_list)
