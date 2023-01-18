from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple = SimpleReport.generate(list)
        products = Counter(item['nome_da_empresa'] for item in list)
        stored = ''

        for company in products:
            stored += f'- {company}: {products[company]}\n'

        return (
          f"{simple}\n"
          f"Produtos estocados por empresa:\n"
          f"{stored}"
        )
