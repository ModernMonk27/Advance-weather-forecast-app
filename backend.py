import requests

Api_key = "8a94c1129477ba01257317ef14d3d955"
def get_data(place, days=None, kind=None):

    url =f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={Api_key}"

    response = requests.get(url)

    data = response.json()

    return data


if __name__ == "__main__":
    print(get_data(place="ooty"))

