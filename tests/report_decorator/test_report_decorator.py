from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    product = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco",
        }
    ]

    report_deco = ColoredReport(SimpleReport).generate(product)
    assert (
        report_deco
        == "\033[32mData de fabricação mais antiga:\033[0m "
        + "\033[36m2022-04-04\033[0m"
        + "\n\033[32mData de validade mais próxima:\033[0m "
        + "\033[36m2023-02-09\033[0m"
        + "\n\033[32mEmpresa com mais produtos:\033[0m "
        + "\033[31mForces of Nature\033[0m"
    )
