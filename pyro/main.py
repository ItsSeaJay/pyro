import argparse
import sys
import os
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
		if os.path.exists(args.new):
			source = 'CodeIgniter-3.1.9'
			destination = args.new
			choice = ''

			# Warn the user that the project's folder isn't empty
			# and give them the option of cancelling
			while choice != 'Y' and choice != 'n':
				choice = input('WARNING: Folder isn\'t empty. Overwrite? (Y/n):')

				if choice != 'Y' and choice != 'n':
					print('ERROR: Invalid choice. Enter only \'Y\' or \'n\'')

			if choice == 'Y':
				copy_tree(source, destination)
		else:
			# TODO: Make this sensitive to the version number
			source = 'CodeIgniter-3.1.9'
			destination = args.new

			os.makedirs(args.new)
			copy_tree(source, destination)

		print('Done.')

if __name__ == '__main__':
	main()
