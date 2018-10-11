import feedparser
import os

from utils.file import *

class Installer:
	def __init__(self):
		pass

	def install(self, destination, version):
		target = (version or self.get_latest_version())

		if version_on_disk(target):
			# Obtain the source of the local CodeIgniter folder on disk
			source = 'CodeIgniter/' + target

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

	def get_latest_version(self):
		versions = self.get_versions()

		# Assuming that the list is sorted in descending order
		return versions[0]

	'''Determines whether the codeigniter version is available locally.'''
	def version_on_disk(self, version):
		for subdirectory in os.walk('codeigniter'):
			if version == subdirectory:
				return True

		return False
