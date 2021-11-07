

from Fly import *
from Quack import *


class Duck:
    flyBehavior = None
    quackBehavior = None

    def __init__(self, fb: FlyBehavior = None, qb: Quack = None):
        self.flyBehavior = fb
        self.quackBehavior = qb

    def setFlyBehavior(self, fb: FlyBehavior):
        self.flyBehavior = fb

    def setQuackBehavior(self, qb: QuackBehavior):
        self.quackBehavior = qb

    def performFly(self):
        self.flyBehavior.fly()

    def performQuack(self):
        self.quackBehavior.quack()

    @staticmethod
    def swim():
        print("all duck float, even decoys.")

    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        super().display()
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        super(ModelDuck, self).__init__()
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm a model duck.")


class RedHeadDuck(Duck):
    def __init__(self):
        super(RedHeadDuck, self).__init__()
        self.flyBehavior = FlyWithWings()
        self.quackBehavior = Quack()

    def display(self):
        print("I'm a real Red Headed duck.")


class DecoyDuck(Duck):
    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.setFlyBehavior(FlyNoWay())
        self.setQuackBehavior(MuteQuack())

    def display(self):
        print("I'm a duck Decoy.")


class RubberDuck(Duck):
    def __init__(self):
        super(RubberDuck, self).__init__()
        self.flyBehavior = FlyNoWay()
        self.quackBehavior = Squeak()

    def display(self):
        print("I'm a rubber duckie")
