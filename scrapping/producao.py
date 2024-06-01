import json
from bs4 import BeautifulSoup
from scrapping.utils import fetch_page
from scrapping.utils import URL_SITE


def get_data_from_producao(ano=None):
    url = f"http://{URL_SITE}/index.ph?opcao=opt_02"
    if ano and 1970 <= ano <= 2023:
        url += f"&ano={ano}"
    html = fetch_page(url)
    if html:

        soup = BeautifulSoup(html, 'html.parser')

        categories_data = []
        for category_row in soup.find_all('td', class_='tb_item'):
            category_data = extract_category_data(category_row.parent)
            categories_data.append(category_data)

        tfoot = soup.find('tfoot', class_='tb_total')
        total_value = tfoot.find_all('td')[-1].get_text(strip=True)

        # Create the final dictionary
        data = {
            'categories': categories_data,
            'total': total_value
        }

        # Convert to JSON
        json_data = json.dumps(data, indent=4)
        return json_data


def extract_category_data(category_row):
    categoria = category_row.find_all('td')[0].get_text(strip=True)
    total = category_row.find_all('td')[1].get_text(strip=True)
    subitems = []

    for subitem_row in category_row.find_next_siblings('tr'):
        if 'tb_item' in subitem_row.find('td')['class']:
            break
        produto = subitem_row.find_all('td')[0].get_text(strip=True)
        valor = subitem_row.find_all('td')[1].get_text(strip=True)
        subitems.append({'produto': produto, 'valor': valor})

    return {'categoria': categoria, 'total': total, 'subitems': subitems}
