class QuackBehavior:
    def quack(self):
        pass


class FakeQuack(QuackBehavior):
    def quack(self):
        print("Qwak")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Slience >>")


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")
