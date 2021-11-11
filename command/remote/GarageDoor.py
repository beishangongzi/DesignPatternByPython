class GarageDoor:

    def __init__(self, location: str):
        self.location = location

    def up(self):
        print(self.location + " garage Door is Up")

    def down(self):
        print(self.location + " garage Door is Down")

    def stop(self):
        print(self.location + " garage Door is Stopped")

    def lightOn(self):
        print(self.location + " garage light is isOn")

    def lightOff(self):
        print(self.location + " garage light is off")
