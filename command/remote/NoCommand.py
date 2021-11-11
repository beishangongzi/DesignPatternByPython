from command.remote.Command import Command


class NoCommand(Command):
    def execute(self) -> None:
        pass
