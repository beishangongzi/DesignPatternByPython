from observer.simple.Observer import Observer
from observer.simple.Subject import Subject


class SimpleObserver(Observer):
    def __init__(self, simpleSubject: Subject):
        self.simpleSubject = simpleSubject
        self.value = 0
        self.simpleSubject.registerObserver(self)

    def update(self, value):
        self.value = value
        self.display()

    def display(self):
        print("Value: " + self.value.__str__())



