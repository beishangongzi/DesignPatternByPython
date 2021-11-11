from command.remotewithUndo.Command import Command
from command.remotewithUndo.Light import Light


class LivingroomLightOffCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()