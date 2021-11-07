from observer.simple.Subject import Subject
from observer.simple.Observer import Observer


class SimpleSubject(Subject):
    value = 0
    observers = []

    def __init__(self):
        super(SimpleSubject, self).__init__()

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        self.observers.remove(o)

    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.value)





