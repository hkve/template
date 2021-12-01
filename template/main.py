import json
import shutil
import pathlib as pl
import subprocess
from template.utils import ask_user, write_config

def copy_template(template_name, templates, paths, check_exsits=True, new_name=None, open_editor=False, editor=None):
	if not template_name in templates.keys():
		print(f'COPY ERROR: the template {template_name} is not found in {paths["templates_config"]}')
		exit()

	if new_name is None:
		new_name = templates[template_name]

	old = paths["templates"].joinpath(templates[template_name])
	new = pl.Path(new_name)

	preform_copy = True

	if new.exists() and check_exsits:
		question = f"The file {new} already exsists here, copying to this loaction results in overwriting the file.\nAre you sure you want to continue?"
		preform_copy = ask_user(question)

	if preform_copy:
		shutil.copy(old, new)

		if open_editor:
			subprocess.run([editor, new])

def list_templates(templates):
	print("Your current templates:")
	print("-----------------------")
	for key, value in templates.items():
		print(f"{key:<20}{value:<20}") 

def add_template(new_file, new_name, templates, paths, remove=False):
	new_file = pl.Path(new_file)

	try:
		shutil.copy(new_file, paths["templates"].joinpath(new_file.name))
	except:
		print(f"The file {new_file} chould not be added to templates, are you sure it's a file?")
		exit()

	templates[new_name] = new_file.name

	write_config(templates, paths["templates_config"])

	if remove:
		new_file.unlink()

def remove_template(name, templates, paths):
	if name not in templates.keys():
		print(f"Cannot remove {name} from templates, since it is not saved in templates config")
		exit()

	tempate_path = paths["templates"].joinpath(templates[name])
	tempate_path.unlink()

	templates.pop(name)

	write_config(templates, paths["templates_config"])

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