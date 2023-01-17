from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(list):
        companies = [company["nome_da_empresa"] for company in list]
        inventoried_company = dict()
        for company in companies:
            if company in inventoried_company:
                inventoried_company[company] += 1
            else:
                inventoried_company[company] = 1
        inventoried = inventoried_company.items()
        product = ""
        simple_report = SimpleReport.generate(list)
        for name, quantity in inventoried:
            product += f"- {name}: {quantity}/n"

        return (
            f"{simple_report}/n"
            f"Produtos estocados por empresa:/n"
            f"{product}"
        )
