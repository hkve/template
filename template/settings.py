def list_settings(settings):
	print("Your current settings:")
	print("----------------------")
	for key, value in settings.items():
		print(f"{key:<20}{value:<20}")

def change_setting(setting, state, settings, paths):
	if not setting in settings.keys():
		print(f"{setting} is not an avalible setting name, check the possible settings by typing")
		print("template settings -l")
		exit()

	setting_type = type(settings[setting])
	try:
		if setting_type is not bool:
			state = setting_type(state)
		else:
			if state.lower() in ["1", "true"]:
				state = 1
			elif state.lower() in ["0", "false"]:
				state = 0
			else: 
				print(f"Chould not covert {state} to bool, please try 1/true/True or 0/false/False") 
	except TypeError:
		print(f"The state {state} is not a valid input for {setting}, excepted input covertible to {setting_type}")
		exit()

	settings[setting] = state
	write_config(settings, paths["settings_config"])