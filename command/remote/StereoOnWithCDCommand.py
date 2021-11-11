from command.remote.Command import Command


class StereoOffCommand(Command):

	def __init__(self, stereo):
		self.stereo = stereo

	def execute(self):
		self.stereo.on()
		self.stereo.setCD()
		self.stereo.setVolume(11)
