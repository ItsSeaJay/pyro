def get_choice(prompt):
	choice = input(prompt)
	error_message = 'ERROR: Invalid choice. Enter only \'Y\' or \'n\''

	while choice != 'Y' and choice != 'n':
		print(error_message)

		choice = input(prompt)

	return choice
