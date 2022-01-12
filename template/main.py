import json
import shutil
import pathlib as pl
import subprocess
from template.utils import ask_user, write_config

def copy(old, new):
	is_file = old.is_file()
	is_folder = old.is_dir()

	path_info = "object"
	try:
		if is_file:
			path_info = "file"
			shutil.copy(old, new)
		elif is_folder:
			path_info = "folder"
			shutil.copytree(old, new, dirs_exist_ok=True)
		else:
			print(f"COPY ERROR: The {obj} {old} is of unknown type. Are you sure it is a file or folder?")
			exit()
	except Exception as error:
		print(f"Unkown error with {path_info} copying from {old} to {new}")
		print(error)
		exit()

def delete(path):
	is_folder = path.is_dir()

	try:
		if is_folder:
			shutil.rmtree(path)
		else:
			path.unlink()
	except Exception as error:
		print(f"Error in remove with {path}")
		print(error)
		exit()

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
		copy(old, new)

		if open_editor:
			subprocess.run([editor, new]) 

def add_template(new_file, new_name, templates, paths, remove=False):
	new_file = pl.Path(new_file)

	copy(new_file, paths["templates"].joinpath(new_file.name))

	templates[new_name] = new_file.name

	write_config(templates, paths["templates_config"])

	if remove:
		delete(new_file)

def remove_template(name, templates, paths):
	if name not in templates.keys():
		print(f"Cannot remove {name} from templates, since it is not saved in templates config")
		exit()

	template_path = paths["templates"].joinpath(templates[name])
	templates.pop(name)
	write_config(templates, paths["templates_config"])

	template_path = pl.Path(template_path)
	if template_path.exists():
		delete(template_path)