class Beverage:
    description = 'Unknown Beverage'

    def getDescription(self):
        return self.description

    def cost(self) -> float:
        pass


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return .99


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return .89
