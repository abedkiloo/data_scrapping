# import requests module
import datetime

import pandas as pd
import requests
from requests_html import HTML


def url_to_txt(url, file_name="files/world.txt"):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(file_name, 'w') as f:
            f.write(r.text)
        return html_text
    return ""


def convert_to_list_of_list(data_object, year):
    # get the html data
    html_data = HTML(html=data_object)

    # get the table with contain the data
    table_class = ".imdb-scroll-table"
    r_table = html_data.find(table_class)
    table_data = []
    header_name = []

    if len(r_table) == 1:
        # format data to list of list
        parsed_table = r_table[0]
        rows = parsed_table.find("tr")

        # the header
        header_row = rows[0]
        header_row_col = header_row.find("th")
        # get the header names
        header_name = [x.text for x in header_row_col]

        # don't iterate through header elements
        for row in rows[1:]:
            cols = row.find("td")

            row_data = []
            # get index
            for i, col in enumerate(cols):
                # print(i, col.text, "\n\n")
                row_data.append(col.text)
            table_data.append(row_data)
    put_data_to_csv(table_data, header_name, file_name=f"movies_{year}.csv")


def put_data_to_csv(data, headers, file_name=None):
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(f'files/{file_name}', index=False)


def execute(start_year=None, years_ago=5):
    if start_year is None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert isinstance(years_ago, int)
    assert len(f"{start_year}") == 4
    for i in range(0, years_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}"
        html_text = url_to_txt(url)
        convert_to_list_of_list(html_text, start_year)
        print(f"completed year {start_year}")
        start_year -= 1


if __name__ == "__main__":
    execute()
