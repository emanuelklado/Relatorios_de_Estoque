from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list) -> str:
        count_products_from_corps = Counter(
            [product["nome_da_empresa"] for product in products]
        ).most_common()

        def iterate_products_from_corps(list: list) -> str:
            result = ""
            for product in list:
                result += f"- {product[0]}: {product[1]}\n"
            return result

        return (
            f"{super().generate(products)}\n"
            f"Produtos estocados por empresa:\n"
            f"{iterate_products_from_corps(count_products_from_corps)}"
        )
