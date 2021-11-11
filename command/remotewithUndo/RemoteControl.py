from command.remotewithUndo.Command import Command
from command.remotewithUndo.NoCommand import NoCommand


class RemoteControl:
    def __init__(self):
        self.onCommands = [Command()] * 7
        self.offCommands = [Command()] * 7

        noCommand = NoCommand()

        for i in range(7):
            self.onCommands[i] = noCommand
            self.offCommands[i] = noCommand

        self.undoCommand = noCommand

    def setCommand(self, slot: int, onCommand: Command, offCommand: Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand

    def onButtonWasPushed(self, slot: int):
        self.undoCommand = self.onCommands[slot]
        self.onCommands[slot].execute()

    def offButtonWasPushed(self, slot: int):
        self.undoCommand = self.offCommands[slot]
        self.offCommands[slot].execute()

    def undoButtonWasPushed(self):
        self.undoCommand.undo()

    def __str__(self):
        message = ""
        message += "\n------Remote Control------\n"
        for i in range(len(self.onCommands)):
            message += "[slot " + i.__str__() + "] " + type(self.onCommands[i]).__name__ + \
                "     " + type(self.offCommands[i]).__name__ + "\n"

        return message
