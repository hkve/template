from template.utils import write_config

def list_settings(settings):
	"""
	List the currents settings. 

	Args:
		settings (dict[str: str/bool]): Dict with settings. Setting name as key with the state as value 
	"""

	print("Your current settings:")
	print("----------------------")
	for key, value in settings.items():
		print(f"{key:<20}{value:<20}")

def change_setting(setting, state, settings, paths):
	"""
	Change setting with value state and write to settings config. Makes sure setting
	is a valid key in settings and that the datatype makes sense. 

	Args:
		setting (str): Setting to write to
		state (str/bool): Value to write to setting
		settings (dict[str: str/bool]): Dict containing current settings
		paths (dict[str: PosixPath]): Dict containg paths 
	"""

	# Check if valid setting name
	if not setting in settings.keys():
		print(f"{setting} is not an avalible setting name, check the possible settings by typing")
		print("template settings -l")
		exit()

	# Get expexted type of setting
	setting_type = type(settings[setting])
	try:
		# If setting_type is not bool, convert to same setting as stored in the dict
		if setting_type is not bool:
			state = setting_type(state)

		# If bool, convert input to bool 0/1
		else:
			if state.lower() in ["1", "true"]:
				state = 1
			elif state.lower() in ["0", "false"]:
				state = 0
			else: 
				print(f"Chould not covert {state} to bool, please try 1/true/True or 0/false/False") 
	
	# Catch wrong type 
	except TypeError:
		print(f"The state {state} is not a valid input for {setting}, excepted input covertible to {setting_type}")
		exit()

	# Save the new state 
	settings[setting] = state

	# Write to settings config json
	write_config(settings, paths["settings_config"])