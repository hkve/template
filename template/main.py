import json
import os
import shutil

# Path to git repo here
root = "/home/haakon/Documents/programmering/python/template" 
root += "/template"

# Path to subfolder where you store templates
subfolder ="your_files_here/"

# config filename
config_filename = "config.json"


def read_config():
	config = json.load(open(f"{root}/{config_filename}"))

	options = config["options"]
	templates = config["templates"]

	options["open_editor"] = int(options["open_editor"])

	template_filenames = list(templates.values())
	found_filenames = os.listdir(f"{root}/{subfolder}")
	missing_files = False

	for file in template_filenames:
		if not file in found_filenames:
			print(f"UPSI: File {file} found in {config_filename} but not in {root}/{subfolder} folder")
			missing_files = True

	if missing_files: exit()

	return options, templates

def copy(new_name, template_name):
	shutil.copy(f"{root}/{subfolder}/{template_name}", new_name)


if __name__ == "__main__":
	options, templates = read_config()

	copy("i_need_a_cow.py", templates["cow"])