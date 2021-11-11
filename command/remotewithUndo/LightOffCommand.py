from command.remotewithUndo.Command import Command
from command.remotewithUndo.Light import Light


class LightOffCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()
