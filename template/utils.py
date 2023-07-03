import json
import os
import string

def ask_user(question):
    """
    Simple yes/no screen for user, where the "question" string is asked. Takes y(yes)/n(no)
    as valid inputs. If no valid input is given, the question is asked again.

    Args:
        question (str): What question should be asked for the y/n menu

    Returns:
        (bool): true/false, answer to question
    """
    check = str(input(f"{question} (Y/N): ")).lower().strip()
    try:
        if check[0] in ["y", "yes"]:
            return True
        elif check[0] in ["n", "no"]:
            return False
        else:
            print('Invalid Input')
            return ask_user(question)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user(question)

def new_stored_name(filename, invalid_names, default_msg=True):
    """
    Ask user for a new stored name. Check if there currently exists an equal stored name.

    Args:
        filename (str): The conflicting name of the new file
        invalid_names (list[str]): The current stored files, where the conflic is present.

    Returns:
        new_filename (str): The new non-conflicting name
    """
    if default_msg:
        print(f"There is already a template file/folder stored under the name {filename}")
        print(f"This will overwrite your old template content as well.")
    
    print(f"Please enter a new name for storage:")

    new_filename = str(input(">: ")).strip()

    if new_filename in invalid_names:
        return new_stored_name(new_filename, invalid_names)
    if not is_valid_filename(new_filename):
        print(f"The filename {new_filename} is not valid is invalid or reserved for Windows.")
        return new_stored_name(new_filename, invalid_names, default_msg=False)
    else:
        return new_filename


def is_valid_filename(filename):
    """
    Checks if a string is a valid filename.

    Args:
        filename (str): To check

    Returns
        Boolean: True if filename is valid, False otherwise
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)

    for char in filename:
        if char not in valid_chars:
            return False

    if filename.strip() == '':
        return False

    reserved_filenames = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4',
                          'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3',
                          'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
    if os.name == 'nt':  # Check if running on Windows
        if filename.upper() in reserved_filenames:
            return False

    return True


def write_config(data, path):
    """
    Takes a dict data and writes it in json format to path.

    Args:
        data (dict[str: dict[str: str]]): The data to be written to path
        path: (PosxPath): Path to the file data will be written to 
    """
    with open(path, "w+") as file:
        json.dump(data, indent=4, sort_keys=True, fp=file)