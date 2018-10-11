import feedparser
import os

from utils.file import *

class Installer:
	def __init__(self):
		pass

	def install(self, destination, version):
		if self.version_on_disk(version):
			# Obtain the source of the local CodeIgniter folder on disk
			source = 'CodeIgniter/' + version

			# Move all of the files from the master copy to the project folder
			# copy_tree(source, destination)

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
		subdirectories = get_immediate_subdirectories('codeigniter')

		for subdirectory in subdirectories:
			print(subdirectory)

			if version == subdirectory:
				# Someone could technically spoof this check by creating
				# a folder that matches the pattern,
				# but we're just going to keep things simple for now
				return True

		return False
