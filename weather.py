from tkinter import *
import http.client

weatherdata = ""

def get_zip_code():

    city = Input_Window.get()

    get_weather_data(city)

def get_weather_data(city):

    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': ""
    }

    conn.request("GET", f"/weather?callback=test&units=metric&q={city}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    format_weather(data.decode("utf-8"))
    
def format_weather(weather_data):

    global weatherdata

    weather = list(weather_data.split(","))

    clouds = weather[4].split(":")[1]
    temp = weather[7].split('p":')[1]
    feels_like = weather[8].split('":')[1]
    temp_min = weather[9].split('":')[1]
    temp_max = weather[10].split('":')[1]
    pressure = weather[11].split('":')[1]
    humidity = weather[12].split('":')[1][:-1]
    wind = weather[14].split('ed":')[1]

    weatherdata = f"Clouds: {clouds}\nTemp: {temp} °C\nFeels like: {feels_like} °C\nTemp Min: {temp_min} °C\nTemp Max: {temp_max} °C\nPressure: {pressure} Pa\nHumidity: {humidity} %\nWind: {wind} km/h"

    print(weatherdata)


master = Tk()
master.geometry("300x500")
master.title("Weather App")

Label(master, text="Your City (e.g Cologne):").grid(row=0, pady=(100,0), padx=(20,0))

Input_Window = Entry(master)

Input_Window.grid(row=1, column=0, padx=(20,0))

Button(master, text='Enter', command=get_zip_code).grid(row=2, column=0, padx=(20,0), pady=(10,0))

Output_Window = Text(master, height=9, width=30)
Output_Window.grid(row=3, column=0, pady=(30,0), padx=(20,0))

Output_Window.insert(END, f"{weatherdata}")




master.mainloop()




