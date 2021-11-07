from observer.weatherobservable.WeatherData import WeatherData
from observer.weatherobservable.CurrentConditionsDisplay import CurrentConditionsDisplay
from observer.weatherobservable.ForecastDisplay import ForecastDisplay
from observer.weatherobservable.StatisticsDisplay import StatisticsDisplay


def main():
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay = ForecastDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 67, 19.4)


if __name__ == '__main__':
    main()