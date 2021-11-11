from command.remote.Command import Command
from command.remote.GarageDoor import GarageDoor


class GarageDoorDownCommand(Command):
    def __init__(self, garageDoor: GarageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()
