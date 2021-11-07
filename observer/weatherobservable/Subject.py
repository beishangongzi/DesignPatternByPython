from observer.weatherobservable.Observer import Observer


class Subject:
    def registerObserver(self, observer: Observer):
        pass

    def removeObserver(self, observer: Observer):
        pass

    def notifyObservers(self):
        pass
