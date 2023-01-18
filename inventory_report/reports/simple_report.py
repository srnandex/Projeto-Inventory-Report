from datetime import datetime
import statistics


class SimpleReport:
    @classmethod
    def generate(cls, list):
        fabric = min(
            [product["data_de_fabricacao"] for product in list]
        )

        validade = min(
            [product["data_de_validade"] for product in list
                if product["data_de_validade"] > str(datetime.today())]
        )

        companys = [company['nome_da_empresa'] for company in list]
        mais_produtos = statistics.mode(companys)

        return (
          f"Data de fabricação mais antiga: {fabric}\n"
          f"Data de validade mais próxima: {validade}\n"
          f"Empresa com mais produtos: {mais_produtos}"
        )
