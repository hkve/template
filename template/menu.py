import os
import pathlib as pl

def get_object_type(path):
	is_file, object_string = None, "?"
	if path.is_file():
		is_file, object_string = True, "file"

	if path.is_dir():
		is_file, object_string = False, "dir"

	return is_file, object_string

def get_object_size(path, is_file):
	if is_file is None:
		return None
	if is_file:
		return os.path.getsize(path)
	if not is_file:
		total_size = 0
		for dirpath, dirnames, filenames in os.walk(path):
			for f in filenames:
				fp = os.path.join(dirpath, f)
				total_size += os.path.getsize(fp)
		return total_size
	
def get_size_unit(size):
	"""
	Converts the given size in bytes to the appropriate magnitude (kB, MB, GB, TB).
	"""
	units = ["bytes", "kB", "MB", "GB", "TB"]
	magnitude = 0

	while size >= 1024 and magnitude < len(units) - 1:
		size /= 1024
		magnitude += 1

	return f"{size:.1f}" + " " + units[magnitude]

def list_templates(templates, templates_path):
	print("Your current templates:")
	print("-"*60)
	for key, value in templates.items():
		path = templates_path.joinpath(pl.Path(value))
		is_file, object_string = get_object_type(path)
		size = get_object_size(path, is_file)
		size = get_size_unit(size)

		print(f"{key:<20}{value:<20}{object_string:<10}{size:<20}")