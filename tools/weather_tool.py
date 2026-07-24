from weather_service import get_weather



def weather_information(city):

    data = get_weather(city)


    if data.get("cod") != 200:

        return {

            "error":
            "City not found"

        }



    return {


        "Location":
        data["name"],


        "Country":
        data["sys"]["country"],


        "Temperature":
        f'{data["main"]["temp"]} °C',


        "Humidity":
        f'{data["main"]["humidity"]} %',


        "Weather":
        data["weather"][0]["description"].title()

    }
