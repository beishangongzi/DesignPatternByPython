from observer.weatherobservable.DisplayElement import DisplayElement
from observer.weatherobservable.Observer import Observer
from observer.weatherobservable.WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    temperature = 0.0
    humidity = 0.0

    def __init__(self, weatherData: WeatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: " + self.temperature.__str__() + "F degrees and " + self.humidity.__str__() + "% humidity")


