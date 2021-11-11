from command.remotewithUndo.Command import Command
from command.remotewithUndo.GarageDoor import GarageDoor


class GarageDoorUpCommand(Command):
    def __init__(self, garageDoor: GarageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.up()

    def undo(self):
        self.garageDoor.down()


