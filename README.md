## Template script, for copying code snippets anywhere from the terminal. 

### Install:
First clone this repo to your local computer. 

```bash
git clone git@github.com:hkve/template.git
```

Now navigate into the git repo

```bash
cd template 
```

From here, copy the absolute file path to the git repo. Type "pwd" and copy the file path. 
```bash
pwd
>>> /home/user/some/path/here/template
```

After you have copied the file path, open the *main.py* file. Set the "root" variable to be this file path, remember to not end the path with a /. 

```python
import json
import os
import shutil

root = "/home/user/some/path/here/template" # HERE
```

Lastly navigate to the main git folder (where bin, template subfolders and setup.py is located) and type 

```bash
pip3 install . --user
```

It should now be installed. Navigate to some random folder and type 

```bash
template cow
```

A file named cow.py should appear in your directory. If it doesn't send me an e-mail. 

### Add templates

In the template subfolder a file named *config.json* should be located. It should look like 

```json
{
	"options":
	{	
		"editor": "subl", 
		"open_editor": "0"  
	},

	"templates": 
	{
		"cow": "cow.py", 
		"cat": "cat.txt"
	}
}
```

Change the "editor" value to whatever bash command you use to open your favorite text editor. If you want the editor to open after the template has been copied, 
change the "open_editor" value to "1". You can add templates to the program by simply adding a new line under "templates". If i want to add a template named 
"index.html", I first write my template and add it to the *your_files_here* folder. Then if i want the alias for this template to be "html" I change my config.json file to:

```json
{
	"options":
	{	
		"editor": "subl", 
		"open_editor": "0"  
	},

	"templates": 
	{
		"cow": "cow.py", 
		"cat": "cat.txt",
		"html": "index.html"
	}
}
```

Now I have added a template to the program, with the alias "html". You DO NOT have to reinstall the package after new templates are added. To copy this file anywhere type.

```Bash
template html
```

To rename the copied file (such that the new file has the content of index.html, but a new name) use the -f flag.

```Bash
template html -f new_name.html
``` 
