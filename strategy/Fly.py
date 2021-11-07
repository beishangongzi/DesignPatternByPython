class FlyBehavior:
    def fly(self):
        pass


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I am flying")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket.")
