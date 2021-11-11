from command.remotewithUndo.Command import Command
from command.remotewithUndo.GarageDoor import GarageDoor


class GarageDoorDownCommand(Command):

    def __init__(self, garageDoor: GarageDoor):
        self.garageDoor = garageDoor

    def execute(self):
        self.garageDoor.down()

    def undo(self):
        self.garageDoor.up()


