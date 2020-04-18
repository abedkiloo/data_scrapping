# import requests module
import requests


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
