import pathlib as pl
import json

def get_cow():
	return r'''a=r"""
 ________________________________________
/ If you see this, all is good           \
\ Have a nice day!                       /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""


print(a)
	'''
def mk_default_template(templates_config, templates_folder):
	# Path to cow example
	cow_path = templates_folder.joinpath("cow.py")

	# Make a cow example in templates_folder
	with open(cow_path, "w+") as file: 
		file.write(get_cow())

	templates = {"cow": "cow.py"}

	# Make templates json
	with open(templates_config, "w+") as file: 
		json.dump(templates, indent=4, sort_keys=True, fp=file)

def mk_default_settings(settings_config):
	default_settings = {
		"editor": "subl", 
		"open_editor": "0",
		"ask_if_exsists": "1"
	}

	with open(settings_config, "w+") as file:
		json.dump(default_settings, indent=4, sort_keys=True, fp=file)


def load_paths():
	directory = pl.Path(__file__).parent

	templates_folder =  directory.joinpath("stored_templates")
	templates_config = directory.joinpath("templates.json")
	settings_config = directory.joinpath("settings.json")

	if not templates_folder.is_dir():
		templates_folder.mkdir()
		print(f"WRITE ACTION: wrote {templates_folder}")

	if not templates_config.is_file():
		mk_default_template(templates_config, templates_folder)
		print(f"WRITE ACTION: Wrote {templates_config}")

	if not settings_config.is_file():
		mk_default_settings(settings_config)
		print(f"WRITE ACTION: Wrote {settings_config}")

	paths = {
	"templates": templates_folder,
	"templates_config": templates_config,
	"settings_config": settings_config 
	}

	return paths

def load_templates(paths=None):
	if paths is None:
		paths = load_paths()

	templates_path = paths["templates_config"]

	with open(templates_path, "r") as file:
		templates = json.load(file)

	return templates

def load_settings(paths=None):
	if paths is None:
		paths = load_paths()

	settings_path = paths["settings_config"]

	with open(settings_path, "r") as file:
		settings = json.load(file)

	settings["open_editor"] = bool(settings["open_editor"])
	settings["ask_if_exsists"] = bool(settings["ask_if_exsists"])

	return settings

if __name__ == "__main__":
	paths = load_paths()
	templates = load_templates(paths)
	settings = load_settings(paths)

	assert templates == load_templates()
	assert settings == load_settings()