from command.remote.Command import Command
from command.remote.Hottub import Hottub


class HottubOffCommand(Command):

	def __init__(self, hottub: Hottub):
		self.hottub = hottub

	def execute(self):
		self.hottub.onFun()
		self.hottub.heat()
		self.hottub.bubblesOn()

