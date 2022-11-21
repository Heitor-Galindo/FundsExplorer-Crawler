from unidecode import unidecode

data = []


def transform_head(table):
    table_head = table.find('thead')
    rows = table_head.find_all('tr')
    for row in rows:
        columms = row.find_all('th')
        columm_data = [unidecode(columm.get_text(separator="_").strip()).upper().replace(' ', '_')
                       for columm in columms]
        data.append([columm for columm in columm_data])
    return data


def transform_body(table):
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        columms = row.find_all('td')
        columm_data = [columm.text.replace('R$', '').replace('%', '').replace('.0', '').replace(
            '.', '').replace('N/A', '').replace(',', '.').strip() for columm in columms]
        data.append([columm for columm in columm_data])
    return data
