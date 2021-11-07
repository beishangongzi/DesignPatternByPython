from observer.weatherobservable.DisplayElement import DisplayElement
from observer.weatherobservable.Observer import Observer
from observer.weatherobservable.WeatherData import WeatherData


class ForecastDisplay(Observer, DisplayElement):
    currentPressure = 29.92
    lastPressure = 0
    weatherData = None

    def __init__(self, weatherData: WeatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def updata(self, temp: float, humidity: float, pressure: float):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure
        self.display()

    def display(self):
        print("Forecast: ")
        if self.currentPressure > self.lastPressure:
            print("improving weather on the way.")
        elif self.currentPressure == self.lastPressure:
            print("More of the same")
        else:
            print("Watch out for cooler, rainy weather.")