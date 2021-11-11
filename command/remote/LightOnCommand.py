from command.remote.Command import Command
from command.remote.Light import Light


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()
