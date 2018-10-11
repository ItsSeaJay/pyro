import os
import shutil

from utils.file import *

def file_get_contents(path):
	with open(path, 'r') as file:
		contents = file.read()

	return contents

# Modified from this StackOverflow post:
# https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth#12514470
def copy_tree(source, destination, symlinks = False, ignore = None):
	for item in os.listdir(source):
		s = os.path.join(source, item)
		d = os.path.join(destination, item)

		print('Copying', os.path.abspath(s), 'to', os.path.abspath(d), '...')

		if os.path.isdir(s):
			if os.path.exists(d):
				shutil.rmtree(d)

			shutil.copytree(s, d, symlinks, ignore)
		else:
			if os.path.exists(d):
				os.remove(d)

			shutil.copy2(s, d)

def get_immediate_subdirectories(path):
	return [name for name in os.listdir(path)
		if os.path.isdir(os.path.join(path, name))]