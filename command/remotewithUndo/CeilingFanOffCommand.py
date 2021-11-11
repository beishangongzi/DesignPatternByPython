from command.remotewithUndo.CeilingFan import CeilingFan
from command.remotewithUndo.Command import Command


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingFan: CeilingFan):
        self.ceilingFan = ceilingFan
        self.prevSpeed = 0

    def execute(self) -> None:
        self.prevSpeed = self.ceilingFan.getSpeed()
        self.ceilingFan.off()

    def undo(self):
        if self.prevSpeed == CeilingFan.HIGH:
            self.ceilingFan.high()
        elif self.prevSpeed == CeilingFan.MEDIUM:
            self.ceilingFan.medium()
        elif self.prevSpeed == CeilingFan.LOW:
            self.ceilingFan.low()


