import argparse
import sys
from utils.file import file_get_contents

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

	if args.new:
		print(args.new)

if __name__ == '__main__':
	main()
