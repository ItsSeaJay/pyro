import os
import shutil

from utils.file import *

def file_get_contents(path):
	with open(path, 'r') as file:
		contents = file.read()

	return contents

# Modified from this StackOverflow post:
# https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth#12514470
def copy_folder_contents(source, destination, symlinks = False, ignore = None):
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

# Modified from this StackOverflow post:
# https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder-in-python#185941
def delete_folder_contents(source):
	for item in os.listdir(source):
		path = os.path.join(source, item)

		try:
			print('Deleting', os.path.abspath(path), '...')

			if os.path.isfile(path):
				os.unlink(path)
			elif os.path.isdir(path):
				shutil.rmtree(path)
		except Exception as e:
			print(e)

# Taken from this StackOverflow post:
# https://stackoverflow.com/questions/800197/how-to-get-all-of-the-immediate-subdirectories-in-python#800201
def get_immediate_subdirectories(path):
	return [name for name in os.listdir(path)
		if os.path.isdir(os.path.join(path, name))]