import json
import shutil
import pathlib as pl
import subprocess
from template.utils import ask_user, write_config

def copy(old, new):
	"""
	Main copy method. Copies file/folder from path old to path new. Also does some simple error
	handling. 

	Args:
		old (PosixPath): Path to old file/folder
		new (PosixPath): Path to new file/folder
	"""

	if not old.exists():
		print(f"The file/folder {old} does not exists, and could not be copied")
		exit()

	# Get object attributes
	is_file = old.is_file()
	is_folder = old.is_dir()

	# Text for display 
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
	"""
	Main delete function. Takes a file/folder path and deletes it (and its content)

	Args:
		path: (PosixPath): Path to file/folder to delete
	"""

	if not path.exists():
		print(f"The file/folder {old} does not exists, and could not be deleted")
		exit()

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
	"""
	Function to copy a template from the template list and add it to new path. If the file already 
	exsits, a yes/no screen is prompted. Can also open prefered editor from settings if the 
	copy was successful. 

	Args:
		template_name (str): Name of the template to copy, as stored as keys in templates dict
		templates (dict[str: PosixPath]): Dict storing all templates and paths
		paths: (dict[str: PosixPath]): Dict storing all paths
		check_exsits (bool): Optional, check if the path written to already exsists, promts a yes/no screen
		new_name (str): Optional, new name to be given to copied file
		open_editor (bool): Optional, if the editor should be opend after copy
		editor (str): Optional, bash command for prefered editor
	"""
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
	"""
	Adds a template to template dict. Can also optionally remove the source file/folder.

	Args:
		new_file (str): Name of source file/folder to add to templates
		new_name (str): Name to be stored as key in templates
		template (dict[str: PosixPath]): Stored templates
		paths (dict[str: PosixPath]): Stored paths
		remove (bool): Optional, if the source file/folder should be removed after addition  
	"""
	new_file = pl.Path(new_file)

	copy(new_file, paths["templates"].joinpath(new_file.name))

	templates[new_name] = new_file.name

	write_config(templates, paths["templates_config"])

	if remove:
		delete(new_file)

def remove_template(name, templates, paths):
	"""
	Removes a template based on template name. Check if the name is stored as a value in templates.

	Args:
		name (str): Name of the template to remove
		templates (dict[str: PosixPath]): Stored templates
		paths (dict[str: PosixPath]): Stored paths
	"""
	if name not in templates.keys():
		print(f"Cannot remove {name} from templates, since it is not saved in templates config")
		exit()

	template_path = paths["templates"].joinpath(templates[name])
	templates.pop(name)
	write_config(templates, paths["templates_config"])

	template_path = pl.Path(template_path)
	if template_path.exists():
		delete(template_path)