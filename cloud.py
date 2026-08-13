# render_template is a function and request is an object
from flask import Flask, render_template, request
import requests  # this is a requests library. It makes requests to the weather API
app = Flask(__name__)


# this route is allowed to receive both GET and POST requests.
@app.route("/", methods=["GET", "POST"])
def home():
    city = "London"  # Understand how this is over written in your code.
    temperature = None  # Understand what would happen if this line weren't here
    error_message = None
    if request.method == "POST":
        city = request.form["city"]
        if not city:  # if the city is empty
            error_message = "Please enter a location. 🌎"
        else:

            print(city)
            # name=London is our parameter for this api
            response = requests.get(
                # we are using the geocoding api in this app
                f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
            print(response.status_code)
# This line converts the JSON response into a Python object
# so we can work with the data print(response.json())
            data = response.json()
            # If the results list is not empty, continue with the first result.
            if data.get("results"):
                location = data["results"][0]  # results is a list, not a dic

                latitude = location["latitude"]
                longitude = location["longitude"]

                weather_response = requests.get(
                    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
                if weather_response.status_code == 400:
                    error_message = "Your request was invalid."
                elif weather_response.status_code == 500:
                    error_message = "Something went wrong on the weather server."
                elif weather_response.status_code != 200:
                    error_message = "Something went wrong. Please try again."
                else:
                    weather_data = weather_response.json()
                    temperature = weather_data["current"]["temperature_2m"]

                    print(temperature)
                    print(weather_response.status_code)
                    # .json is saying, "Take the JSON data that the weather API sent back and convert it into a Python object so I can work with it."
                    print(weather_response.json())

            else:
                error_message = "Stop making up fake places bruh💢"
    # message is an argument
    # the temperature on the left is from your html; the temperature on the right is from your python file.
    return render_template(
        "cloud.html",
        message="Welcome to CloudNine🌥️",
        city=city,
        temperature=temperature,
        error_message=error_message
    )


@app.route("/about")
def about():
    return "CloudNine is a weather app built with Flaskkkk"


# Flask's request receives a request from the browser.

# Python's requests sends a request to the weather API.
