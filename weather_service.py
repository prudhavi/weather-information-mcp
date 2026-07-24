import requests

from config import API_KEY, BASE_URL



def get_weather(city):

    url = f"{BASE_URL}/weather"


    params = {

        "q": city,

        "appid": API_KEY,

        "units": "metric"

    }


    response = requests.get(
        url,
        params=params
    )


    return response.json()
