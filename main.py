from datetime import datetime
import requests


weather_api = "c183b54927b883296dd8e9e384897013"

print("------------- ShapeAI Weather Project -------------\n")

city = input("Enter City Name : ")

weather_data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + weather_api).json()

info = "\n---------------------------------------------------\n"
info += "           "+city.upper()+" || "+datetime.now().strftime("%H:%M:%S - %d %b, %Y")+"     \n"
info += "---------------------------------------------------\n"

info += "Weather : " + weather_data["weather"][0]["main"] + "\n"
info += "Weather Description : " + weather_data["weather"][0]["description"] + "\n"
info += "Temperature : " + str(weather_data["main"]["temp"]) + " °C\n"
info += "Pressure : " + str(weather_data["main"]["pressure"]) + " hPa\n"
info += "Humidity : " + str(weather_data["main"]["humidity"]) + " %\n"
info += "Visibility : " + str(weather_data["visibility"]) + " Metre\n"
info += "Wind Speed : " + str(weather_data["wind"]["speed"]) + " m/s\n"
info += "Clouds : " + str(weather_data["clouds"]["all"]) + " %\n"

print(info)

with open("weather_report.txt","a+") as logfile:
    logfile.write(info)

