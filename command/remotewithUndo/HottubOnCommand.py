from command.remotewithUndo.Command import Command
from command.remotewithUndo.Hottub import Hottub


class HottubOffCommand(Command):

	def __init__(self, hottub: Hottub):
		self.hottub = hottub

	def execute(self):
		self.hottub.onFun()
		self.hottub.heat()
		self.hottub.bubblesOn()

	def undo(self):
		self.hottub.cool()
		self.hottub.off()


