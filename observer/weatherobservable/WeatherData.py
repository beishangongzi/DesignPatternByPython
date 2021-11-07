from observer.weatherobservable.Observer import Observer
from observer.weatherobservable.Subject import Subject


class WeatherData(Subject):
    observers = []
    temperature = 0.0
    humidity = 0.0
    pressure = 0.0

    def __init__(self):
        super(WeatherData, self).__init__()

    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    def getTemperature(self) -> float:
        return self.temperature

    def getHumidity(self) -> float:
        return self.humidity

    def getPressure(self) -> float:
        return self.pressure

