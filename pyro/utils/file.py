import shutil

'''Obtains the contents of a text file as a Python string.'''
def file_get_contents(path):
	with open(path, r) as file:
		contents = file.read()

	return contents