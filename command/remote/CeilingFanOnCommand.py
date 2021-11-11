from command.remote.CeilingFan import CeilingFan
from command.remote.Command import Command


class CeilingFanOnCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan

    def execute(self) -> None:
        self.ceilingFan.high()
