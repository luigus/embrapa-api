import requests

URL_SITE = "vitibrasil.cnpuv.embrapa.br"


def fetch_page(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
