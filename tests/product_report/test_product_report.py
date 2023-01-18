from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "CADEIRA",
        "Forces of Nature",
        "2022-04-04",
        "2023-02-09",
        "FR48",
        "Conservar em local fresco",
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto} "
        f"fabricado em {product.data_de_fabricacao} "
        f"por {product.nome_da_empresa} com validade "
        f"até {product.data_de_validade} "
        f"precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
    assert type(product.__repr__())
