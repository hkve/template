## Template script, for copying code snippets anywhere from the terminal. 

### Install:
First clone this repo to your local computer. 

```bash
git clone git@github.com:hkve/template.git
```

Enter the main git folder (where bin, template subfolders and setup.py are located) and type 

```bash
pip3 install . --user
```

It should now be installed. An example cow should be there to help you. Type 

```bash
template get cow 
```

A file named cow.py should appear in your directory.  

### Usage

Templates can be stored from the command line. Assuming I have a file named cat.c, and I want to add it to my templates under the name cat, write.

```bash
template add cat.txt cat
```
The cat should now be added to your available templates. You can check your templates by:

```bash
template list
```
If I decide that I do not want the file "cat.txt" among my templates, I can write:

```bash
template remove cat
```
Again I can check my available templates and make sure it is gone

### Settings
Currently, very few setting are available, if you have any ideas/request please send me an e-mail. You can check you current settings by typing 

```bash
template settings -l
```
To change a settings, use the "-c" flag followed by setting name and state. For instance if I open my favourite text editor from the command line using the alias "code", I can add this to the settings by typing:

```bash
template settings -c editor code
```
The settings should now be updated. If you encounter any problems, feel free to send me an e-mail.
