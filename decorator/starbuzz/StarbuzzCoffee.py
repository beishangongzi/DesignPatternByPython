from Beverage import Espresso, DarkRoast
from CondimentDecorator import Mocha


class StarbuzzCoffee:
    @staticmethod
    def main():
        beverage = Espresso()
        print(beverage.getDescription() + " $" + beverage.cost().__str__())

        beverage2 = DarkRoast()
        beverage2 = Mocha(beverage2)
        beverage2 = Mocha(beverage2)
        print(beverage2.getDescription() + " $" + beverage2.cost().__str__())


if __name__ == '__main__':
    starbuzzCoffee = StarbuzzCoffee()
    starbuzzCoffee.main()
