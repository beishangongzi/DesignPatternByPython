from command.remote.CeilingFan import CeilingFan
from command.remote.Command import Command


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan

    def execute(self) -> None:
        self.ceilingFan.off()
