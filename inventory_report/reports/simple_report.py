from datetime import date


class SimpleReport:
    @classmethod
    def generate(cls, list):
        company = [product["nome_da_empresa"] for product in list]
        old_date = cls.old_date(list)
        expired_date = cls.expired_date(list)
        more_product = max(set(company), key=company.count)

        return (
            f"Data de fabricação mais antiga: {old_date}\n"
            f"Data de validade mais próxima: {expired_date}\n"
            f"Empresa com mais produtos: {more_product}"
        )

    @classmethod
    def old_date(cls, products):
        dates = [product["data_de_fabricacao"] for product in products]
        return min(dates)

    @classmethod
    def expired_date(cls, products):
        dates = [
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"] > str(date.today())
        ]
        return min(dates)
