import re # Regular expressions (regex)
import os # Operating system

from utils.file import *

class Configurator:
	def __init__(self):
		pass

	'''Uses a regular expression to replace the contents of a config file'''
	def configure(self, file, key, value):
		# Build the file to the config path
		path = 'application/config/' + file + '.php'
		
		if os.path.exists(path):
			# An explanation of this pattern can be found here:
			# https://regex101.com/r/6Pf9c1/7
			# Basically it tries to find a PHP array variable with the same key as
			# the one the user entered, and then splits it into 3 distinct groups
			variable_pattern = r'(\$.*\[\'' + key + r'\'\][ ]*=[ ]*)(.*)(;.*)'
			search = re.search(
				variable_pattern,
				file_get_contents(path)
			)

			# Check whether the search returned anything
			if search:
				# Find the old value we're about to replace
				# NOTE: Regular expressions count from 1 and not 0
				old_value = search.group(2)
				# Regex pattern obtained from this stack overflow post:
				# https://stackoverflow.com/questions/171480/regex-grabbing-values-between-quotation-marks#171499
				quotes_pattern = r'(["\'])(?:(?=(\\?))\2.)*?\1'
				
				# Preserve any quotes in the variable
				# Check if the value we have is a string and there aren't quotes
				# around the new value already
				if re.search(quotes_pattern, old_value) and not re.search(quotes_pattern, value):
					# This value will be a string
					# Automatically surround the value with quotes
					value = '\'' + value + '\''

				# NOTE: The replacement has to be set down here because of the above search
				replacement = r'\1' + value + r'\3'
				configuration = re.sub(
					variable_pattern,
					replacement,
					file_get_contents(path)
				)

				# Write the new configuration to the file
				file_put_contents(path, configuration)
				# Alert the user that we've done that
				print('Changed old', key, 'from', old_value, 'to', value, 'in', os.path.abspath(path))
			else:
				print('ERROR: Unable to find any variables in', os.path.abspath(path), 'with the key', key)
		else:
			print('ERROR: No file named', os.path.abspath(path), 'exists.')