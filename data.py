from utils import query_database, results_to_json


def get_producao_data(year=2022):
    query = f'SELECT Id, control, produto, "{year}"  as "quantidade(L)" FROM Producao;'
    results = query_database(query)
    json_data = results_to_json(results)
    return json_data


def get_comercio_data(year=2022):
    query = f'SELECT Id, control, produto, "{year}" as "quantidade(L)" FROM Comercio;'
    results = query_database(query)
    json_data = results_to_json(results)
    return json_data


def get_processa_data(_type="mesa", year=2022):
    table = "ProcessaMesa"
    if _type == 'semclasse':
        table = "ProcessaSemclass"

    if _type == 'americanas':
        table = "ProcessaAmericanas"

    if _type == 'viniferas':
        table = "ProcessaViniferas"

    query = f'SELECT Id, control, cultivar, "{year}"  as "quantidade(Kg)" FROM {table};'

    results = query_database(query)
    json_data = results_to_json(results)
    return json_data


def get_importacao_data(_type='vinho', year=2022):
    table = "ImpVinhos"

    if _type == 'suco':
        table = "ImpSuco"

    if _type == 'passas':
        table = "ImpPassas"

    if _type == 'frescas':
        table = "ImpFrescas"

    if _type == 'espumantes':
        table = "ImpEspumantes"

    query = f'SELECT Id, "País", "{year}_q" as "quantidade(Kg)", "{year}_v" as "valor (US$)"  FROM {table};'

    results = query_database(query)
    json_data = results_to_json(results)
    return json_data


def get_exportacao_data(_type='vinho', year=2022):
    table = "ExpVinhos"

    if _type == 'suco':
        table = "ExpSuco"

    if _type == 'uva':
        table = "ExpUva"

    if _type == 'espumantes':
        table = "ExpEspumantes"

    query = f'SELECT Id, "País", "{year}_q" as "quantidade(kg)", "{year}_v" as "valor (US$)"  FROM {table};'

    results = query_database(query)
    json_data = results_to_json(results)
    return json_data
