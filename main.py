#@Raynold van der Palm
#weather api

import pyowm

#area
owm = pyowm.OWM('78d912eeb92eb92d282e5237b494a369')
observation = owm.weather_at_place('Den Helder, NL')
weather = observation.get_weather()

#begin tekst
print("Het weerbericht in Den Helder")

#temperatuur
temperature = weather.get_temperature('celsius')['temp']
print(f"Temperatuur: {temperature} graden\n")

#wind
wind = weather.get_wind()['speed']
print(f"Windsnelheid: {wind} m/s\n")

#luchtvochtigheid
humidity = weather.get_humidity()
print(f"Luchtvochtigheid: {humidity}%")



