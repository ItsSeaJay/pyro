from utils.file import *

class Installer:
	def __init__(self):
		pass

	def install(self, destination):
		# Obtain the source of the local CodeIgniter folder on disk
		source = 'CodeIgniter-' + self.get_latest_version()

		# Move all of the files from the master copy to the project folder
		copy_tree(source, destination)

	def get_latest_version(self):
		# TODO: Make this read from the atom releases feed
		return '3.1.9'