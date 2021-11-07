from observer.weatherobservable.DisplayElement import DisplayElement
from observer.weatherobservable.Observer import Observer
from observer.weatherobservable.WeatherData import WeatherData


class StatisticsDisplay(Observer, DisplayElement):
    maxTemp = 0.0
    minTemp = 0.0
    testSum = 0.0
    numReadings = 0

    def __init__(self, weatherData: WeatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.testSum += temp
        self.numReadings += 1
        if(temp > self.maxTemp):
            self.maxTemp = temp
        elif temp < self.minTemp:
            self.minTemp = temp

        self.display()

    def display(self):
        print("AVG/MAX/Min Temperature = " + (self.testSum / self.numReadings).__str__() + "/" + self.maxTemp.__str__() + "/" + self.minTemp.__str__())

