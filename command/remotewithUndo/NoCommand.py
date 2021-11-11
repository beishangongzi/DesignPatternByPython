from command.remotewithUndo.Command import Command


class NoCommand(Command):
    def execute(self) -> None:
        pass

    def undo(self):
        pass
