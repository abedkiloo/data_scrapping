# import requests module
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


url = "https://www.boxofficemojo.com/year/world"
html_text = url_to_txt(url)
html_data = HTML(html=html_text)
# get the table with contain the data
table_class = ".imdb-scroll-table"
r_table = html_data.find(table_class)
table_data = []
header_name = []

if len(r_table) == 1:
    # format data to list of lisr
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

print(header_name)
print(table_data)
