from observer.weatherobservable.DisplayElement import DisplayElement
from observer.weatherobservable.Observer import Observer
from observer.weatherobservable.WeatherData import WeatherData


class HeatIndexDisplay(Observer, DisplayElement):
    heatIndex = 0.0

    def __init__(self, weatherData: WeatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)

    def update(self, t: float, rh: float, pressure: float):
        self.heatIndex = self.computeHeatIndex(t, rh)
        self.display()

    def computeHeatIndex(self, t: float, rh: float):
        index = ((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh)
                         + (0.00941695 * (t * t)) + (0.00728898 * (rh * rh))
                         + (0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
                         (0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *
                                                                                             (rh * rh * rh)) + (
                                     0.00000142721 * (t * t * t * rh)) +
                         (0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +
                         0.000000000843296 * (t * t * rh * rh * rh)) -
                        (0.0000000000481975 * (t * t * t * rh * rh * rh)))
        return index

    def display(self):
        print("Heat index is " + self.heatIndex.__str__())




