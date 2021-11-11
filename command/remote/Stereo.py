class Stereo:

    def __init__(self, location):
        self.location = location

    def on(self):
        print(self.location + " stereo is on")

    def off(self):
        print(self.location + " stereo is off")

    def setCD(self):
        print(self.location + " stereo is set for CD input")

    def setDVD(self):
        print(self.location + " stereo is set for DVD input")

    def setRadio(self):
        print(self.location + " stereo is set for Radio")

    def setVolume(self, volume):
        print(self.location + " stereo volume set to " + volume)
