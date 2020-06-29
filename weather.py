from tkinter import *
import http.client


class Weather():

    def __init__(self):    

        self.master = Tk()
        self.master.geometry("300x500")
        self.master.title("Weather App")

        Label(self.master, text="Your City (e.g Cologne):").grid(row=0, pady=(100,0), padx=(20,0))

        self.Input_Window = Entry(self.master)

        self.Input_Window.grid(row=1, column=0, padx=(20,0))

        Button(self.master, text='Enter', command=self.get_city).grid(row=2, column=0, padx=(20,0), pady=(10,0))

        self.Output_Window = Text(self.master, height=9, width=30)
        self.Output_Window.grid(row=3, column=0, pady=(30,0), padx=(20,0))

        self.Output_Window.insert(END, "")

        self.master.mainloop()


    def get_city(self):

        city = self.Input_Window.get()

        self.get_weather_data(city)

    def get_weather_data(self,city):

        conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

        headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "YOUR API KEY"
        }

        conn.request("GET", f"/weather?callback=test&units=metric&q={city}", headers=headers)

        res = conn.getresponse()
        data = res.read()

        self.format_weather(data.decode("utf-8"))
        
    def format_weather(self, weatherdata):

        weather = list(weatherdata.split(","))

        clouds = weather[4].split(":")[1]
        temp = weather[7].split('p":')[1]
        feels_like = weather[8].split('":')[1]
        temp_min = weather[9].split('":')[1]
        temp_max = weather[10].split('":')[1]
        pressure = weather[11].split('":')[1]
        humidity = weather[12].split('":')[1][:-1]
        wind = weather[14].split('ed":')[1]

        weatherdata = f"Clouds: {clouds}\nTemp: {temp} °C\nFeels like: {feels_like} °C\nTemp Min: {temp_min} °C\nTemp Max: {temp_max} °C\nPressure: {pressure} Pa\nHumidity: {humidity} %\nWind: {wind} km/h"

        #print(weatherdata)

        

        self.Output_Window.delete('1.0', END)

        self.Output_Window.insert(END, weatherdata)

Weather()



