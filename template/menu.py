def list_templates(templates):
	print("Your current templates:")
	print("-----------------------")
	for key, value in templates.items():
		print(f"{key:<20}{value:<20}")