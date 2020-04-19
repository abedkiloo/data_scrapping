import os

import pandas as pd
import requests

v3_api_auth = "dbb41060d34f2ddceb2218bdc1a45390"
v4_auth_key = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkYmI0MTA2MGQzNGYyZGRjZWIyMjE4YmRjMWE0NTM5MCIsInN1YiI6IjVlOWM3MTMzNGE0YmZjMDAxZWQ2ODJiYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GLl3BP1Hz2sFMqHK2zu39jtzh4qHZ571G_wqeKIyE68"
base_url = "https://api.themoviedb.org/3/"
FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
HOST_DIRECTORY = os.path.abspath(os.path.join(FILE_PATH, os.pardir))
PARENT_DIRECTORY = os.path.abspath(os.path.join(HOST_DIRECTORY, os.pardir))


def get_movies_data(url, movie_id=None):
    if not isinstance(movie_id, int):
        return "enter a movie value"

    request_url = f"{url}movie/{movie_id}?api_key={v3_api_auth}"
    request = requests.get(request_url)
    return request


def convert_to_csv(data, header_columns=None, file_name=None):
    movie_data = []
    # for movie in data:
    movie_data.append(data)

    df = pd.DataFrame(movie_data)
    df.to_csv(os.path.join(f"{PARENT_DIRECTORY}", f"files/{file_name}.csv"))
    print(f"saved {file_name}.csv")


if __name__ == "__main__":
    print(PARENT_DIRECTORY)
    request_object = get_movies_data(base_url, 500)
    if not isinstance(request_object, str):
        if request_object.status_code in range(199, 299):
            convert_to_csv(data=request_object.json(), file_name="movies_data")
    else:
        print(request_object)
