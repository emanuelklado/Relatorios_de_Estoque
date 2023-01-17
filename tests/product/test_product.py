from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Modem",
        nome_da_empresa="Brisanet",
        data_de_fabricacao="05-03-2021",
        data_de_validade="05-03-2022",
        numero_de_serie="16835468",
        instrucoes_de_armazenamento="Armazenar em local seco",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Modem"
    assert product.nome_da_empresa == "Brisanet"
    assert product.data_de_fabricacao == "05-03-2021"
    assert product.data_de_validade == "05-03-2022"
    assert product.numero_de_serie == "16835468"
    assert product.instrucoes_de_armazenamento == "Armazenar em local seco"
