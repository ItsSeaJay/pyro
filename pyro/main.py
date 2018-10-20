import argparse
import sys
import os

from installer import Installer
from configurator import Configurator
from utils.file import *
from utils.command_line import *

def main():
	# Create a new ArgumentParser
	# TODO: Fix relative paths when obtaining the description
	description = file_get_contents(get_base_path() + '/config/description.txt')
	parser = argparse.ArgumentParser(description = description)
	
	# Add the list of valid command line arguments to the parser
	# New project
	parser.add_argument(
		'-n',
		'--new',
		help = 'Creates a new CodeIgniter project with a given name',
		metavar = ('NAME', 'VERSION'),
		nargs = 2
	)
	# Versions
	parser.add_argument(
		'-v',
		'--versions',
		help = 'Gets a list of all of the CodeIgniter versions currently installed on disk',
		action = 'store_true' # Don't accept any positional arguments after this one
	)
	# Download CodeIgniter Version version
	parser.add_argument(
		'-d',
		'--download',
		help = 'Downloads the specified CodeIgniter version if it isn\'t already on disk',
		metavar = 'VERSION',
		nargs = 1
	)
	# Configure
	parser.add_argument(
		'-c',
		'--configure',
		help = 'Edits a single value in the configuration files of the current project',
		metavar = ('FILE', 'KEY', 'VALUE'),
		nargs = 3
	)
	# Generate
	parser.add_argument(
		'-g',
		'--generate',
		help = 'Creates a new source file of the given type and name in the current project',
		metavar = ('TYPE', 'NAME'),
		nargs = 2
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
		project_name = args.new[0]
		codeigniter_version = args.new[1]

		if codeigniter_version == 'l' or codeigniter_version == 'latest':
			print('Latest online CodeIgniter version selected (', codeigniter_version, ').')
			codeigniter_version = installer.get_latest_version()

		if os.path.exists(project_name):
			prompt = 'WARNING: Folder isn\'t empty. Overwrite? (Y/n): '
			choice = get_choice(prompt)

			if choice == 'Y':
				installer.install(project_name, codeigniter_version)
		else:
			os.makedirs(project_name)
			installer.install(project_name, codeigniter_version)

		print('Done.')
	elif args.versions:
		versions = os.listdir('codeigniter')

		if len(versions) > 0:
			print('Versions available on disk:')

			for version in versions:
				print(version)
		else:
			print('No valid codeigniter versions currently installed.')
	elif args.download:
		codeigniter_version = args.download[0]
		installer = Installer()

		if codeigniter_version == 'l' or codeigniter_version == 'latest':
			print('Latest online CodeIgniter version selected (', codeigniter_version, ').')
			codeigniter_version = installer.get_latest_version()

		path = 'codeigniter/' + codeigniter_version

		if not os.path.isdir(path):
			installer.download(codeigniter_version)
	elif args.configure:
		configurator = Configurator()
		file = args.configure[0]
		key = args.configure[1]
		value = args.configure[2]

		configurator.configure(file, key, value)
	elif args.generate:
		kinds = [
			'model',
			'view',
			'controller',
			'helper'
		]

		# Iterate through all of the kinds of files to see if the user matched one
		for kind in kinds:
			if args.generate[0] == kind:
				# Generate a class name by capitilizing the first letter
				name = args.generate[1].title().replace(' ', '_')
				# Find the name of the resulting file
				path = 'application/' + kind + 's/' + name + '.php'
				# Get the template as a string
				template =  file_get_contents(get_base_path() + '/templates/' + kind + '.php')

				# Replace the name in the template with the one the user chose
				template = template.replace('{name}', name)

				# Write the filled in template to the path
				file_put_contents(path, template)

				# Print what kind of file we're generating to the console
				print('Generating', kind, 'at', os.path.abspath(path), 'called', name, '...')

	print('Done.')

if __name__ == '__main__':
	main()
