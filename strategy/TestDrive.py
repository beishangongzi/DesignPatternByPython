from Duck import *

mallard = MallardDuck()
mallard.display()
mallard.performQuack()
mallard.performFly()

model = ModelDuck()
model.display()
model.performFly()
model.performQuack()

model.setFlyBehavior(FlyRocketPowered())
model.performFly()