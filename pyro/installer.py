import feedparser
import os
import shutil
import urllib.request
import zipfile

from utils.file import *
from utils.command_line import *

class Installer:
	def __init__(self):
		pass

	def install(self, destination, version):
		if self.version_on_disk(version):
			source = 'codeigniter/' + version

			copy_folder_contents(source, destination)
		else:
			print('CodeIgniter version isn\'t available on disk')
			print('Use the --download command to get it')

	def download(self, version):
		# Download the latest version of CodeIgniter
		url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + version + '.zip'
		path = 'cache/' + version + '.zip'
		source = 'cache/CodeIgniter-' + version
		destination = 'codeigniter/' + version

		print('Downloading', url, '...')

		# Make a request to open the file at the above URL
		with urllib.request.urlopen(url) as response, open(path, 'wb') as archive:
			# Write the binary data from the page to a file on disk
			data = response.read()
			archive.write(data)

		print('Extracting', os.path.abspath(path), 'to', os.path.abspath(destination), '...')

		# Extract the contents to the cache folder
		with zipfile.ZipFile(path, 'r') as archive:
			archive.extractall('cache')

		# Copy the extracted files to the codeigniter folder
		os.makedirs(destination)
		copy_folder_contents(source, destination)

		# Clean the cache after the download has completed
		self.clean_cache()

	def clean_cache(self):
		print('Cleaning pyro cache at', os.path.abspath('cache'), '...')
		delete_folder_contents('cache')

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
		# Get all of the subdirectories at the first level of the codeigniter folder
		subdirectories = get_immediate_subdirectories('codeigniter')

		for subdirectory in subdirectories:
			if version == subdirectory:
				# Someone could technically spoof this check by creating
				# a folder that matches the pattern,
				# but we're just going to keep things simple for now
				return True

		return False
