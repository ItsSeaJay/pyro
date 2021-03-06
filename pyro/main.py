import argparse
import sys
import os
import installer

from utils.file import *

def main():
	# Create a new ArgumentParser
	description = file_get_contents('config/description.txt')
	parser = argparse.ArgumentParser(description = description)
	
	# Add the command line arguments
	parser.add_argument(
		'-n',
		'--new',
		help = 'Creates a new CodeIgniter project with the given name'
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
			choice = ''

			# Warn the user that the project's folder isn't empty
			# and give them the option of cancelling
			while choice != 'Y' and choice != 'n':
				choice = input('WARNING: Folder isn\'t empty. Overwrite? (Y/n):')

				if choice != 'Y' and choice != 'n':
					print('ERROR: Invalid choice. Enter only \'Y\' or \'n\'')

			if choice == 'Y':
				installer.install(args.new)
		else:
			os.makedirs(args.new)
			installer.install(args.new)

		print('Done.')

if __name__ == '__main__':
	main()
