class Light:

    def __init__(self, location: str):
        self.location = location

    def on(self):
        print(self.location + " light is on")

    def off(self):
        print(self.location + " light is off")
