from command.remotewithUndo.Command import Command
from command.remotewithUndo.Stereo import Stereo

class StereoOffCommand(Command):

    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        self.stereo.setCD()
        self.stereo.setVolume(11)

