import feedparser

from utils.file import *

class Installer:
	def __init__(self):
		pass

	def install(self, destination):
		# Obtain the source of the local CodeIgniter folder on disk
		versions = self.get_versions()
		source = 'CodeIgniter-' + versions[0]

		# Move all of the files from the master copy to the project folder
		copy_tree(source, destination)

	def get_versions(self):
		url = 'https://github.com/bcit-ci/CodeIgniter/releases.atom'
		# Parse the atom releases feed for CodeIgniter on GitHub
		atom = feedparser.parse(url)
		versions = []

		# Obtain the version numbers
		for entry in atom.entries:
			versions.append(entry.title)

		return versions