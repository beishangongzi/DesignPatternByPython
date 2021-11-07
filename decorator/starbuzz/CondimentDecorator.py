from Beverage import Beverage


class CondimentDecorator(Beverage):
    beverage = None

    def getDescription(self):
        pass


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Milk"

    def cost(self) -> float:
        return .10 + self.beverage.cost()


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self) -> float:
        return .15 + self.beverage.cost()


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self) -> float:
        return .10 + self.beverage.cost()


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"

    def cost(self) -> float:
        return .20 + self.beverage.cost()
