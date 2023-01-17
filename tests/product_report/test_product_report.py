from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "roteador",
        "brisanet",
        "01-04-2020",
        "02-06-2022",
        78522456,
        "local seco e longe de umidade",
    )

    assert str(product) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
