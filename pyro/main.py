import argparse
import sys
import os

from installer import Installer
from utils.file import *
from utils.command_line import *

def main():
	# Create a new ArgumentParser
	description = file_get_contents('config/description.txt')
	parser = argparse.ArgumentParser(description = description)
	
	# Add the list of valid command line arguments to the parser
	# New project
	parser.add_argument(
		'-n',
		'--new',
		help = 'Creates a new CodeIgniter project with a given name',
		nargs = 1
	)
	# Versions
	parser.add_argument(
		'-v',
		'--versions',
		help = 'Gets a list of all of the CodeIgniter versions currently installed on disk',
		action = 'store_true' # Don't accept any positional arguments after this one
	)
	# download
	parser.add_argument(
		'-d',
		'--download',
		help = 'Downloads the specified codeigniter version if it isn\'t already',
		nargs = 1
	)


	# Parse the arguments sent by the user and store them
	args = parser.parse_args()

	# By default, show the help message
	if len(sys.argv[1:]) == 0:
		parser.print_help()
		parser.exit()

	# React accordingly based on which argument they used
	if args.new:
		installer = Installer()

		if os.path.exists(args.new):
			prompt = 'WARNING: Folder isn\'t empty. Overwrite? (Y/n): '
			choice = get_choice(prompt)

			if choice == 'Y':
				installer.install(args.new, installer.get_latest_version())
		else:
			os.makedirs(args.new)
			installer.install(args.new, installer.get_latest_version())

		print('Done.')
	elif args.versions:
		versions = os.listdir('codeigniter')

		if len(versions) > 0:
			for version in versions:
				print(version)
		else:
			print('No valid codeigniter versions currently installed.')
	elif args.download:
		installer = Installer()
		path = 'codeigniter/' + args.download

		if not os.path.isdir(path):
			installer.download(args.download)

if __name__ == '__main__':
	main()
